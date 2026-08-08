"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeKeyPairsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.key_pair_list


class DescribeKeyPairsResult(TypedDict, closed=True):
    key_pairs: NotRequired["capo_ec2.types.key_pair_list.KeyPairList"]
    """<p>Information about the key pairs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeKeyPairsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "key_pairs" in value:
        import capo_ec2.types.key_pair_list

        capo_ec2.types.key_pair_list.serialize_ec2_query(
            value["key_pairs"], pairs, f"{key_prefix}KeySet"
        )


def deserialize_ec2_query(el: Element) -> DescribeKeyPairsResult:
    out: DescribeKeyPairsResult = {}  # type: ignore[typeddict-item]
    if el.find("keySet") is not None:
        import capo_ec2.types.key_pair_list

        out["key_pairs"] = capo_ec2.types.key_pair_list.deserialize_ec2_query(
            el, "keySet"
        )
    return out
