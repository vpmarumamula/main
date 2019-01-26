
import java.util.*;

public class One {
	public static void main(String[] args) {
		System.out.println("This is the first output");
		List<Integer> items = new ArrayList<Integer>();
		items.add(5);
		for(int i=0;i<items.size();i++) {
			System.out.println(items.get(i));
		}
	}
}