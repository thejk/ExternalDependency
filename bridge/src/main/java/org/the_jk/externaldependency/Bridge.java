package org.the_jk.externaldependency;

class Bridge {
    static String combine(String a, String b) {
        return External.combine(a, b);
    }
}
