"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeKeyPairsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.key_pair_list


class DescribeKeyPairsResult(TypedDict):
    key_pairs: NotRequired["aws_sdk_ec2.types.key_pair_list.KeyPairList"]
    """<p>Information about the key pairs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeKeyPairsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "key_pairs" in value:
        import aws_sdk_ec2.types.key_pair_list

        aws_sdk_ec2.types.key_pair_list.serialize_ec2_query(
            value["key_pairs"], pairs, f"{prefix}.KeySet"
        )


def deserialize_ec2_query(el: Element) -> DescribeKeyPairsResult:
    out: DescribeKeyPairsResult = {}  # type: ignore[typeddict-item]
    if el.find("KeySet") is not None:
        import aws_sdk_ec2.types.key_pair_list

        out["key_pairs"] = aws_sdk_ec2.types.key_pair_list.deserialize_ec2_query(
            el, "KeySet"
        )
    return out
