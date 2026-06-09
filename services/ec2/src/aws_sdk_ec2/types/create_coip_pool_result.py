"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCoipPoolResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.coip_pool


class CreateCoipPoolResult(TypedDict):
    coip_pool: NotRequired["aws_sdk_ec2.types.coip_pool.CoipPool"]
    """<p>Information about the CoIP address pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCoipPoolResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "coip_pool" in value:
        import aws_sdk_ec2.types.coip_pool

        aws_sdk_ec2.types.coip_pool.serialize_ec2_query(
            value["coip_pool"], pairs, f"{prefix}.CoipPool"
        )


def deserialize_ec2_query(el: Element) -> CreateCoipPoolResult:
    out: CreateCoipPoolResult = {}  # type: ignore[typeddict-item]
    child_coip_pool = el.find("CoipPool")
    if child_coip_pool is not None:
        import aws_sdk_ec2.types.coip_pool

        out["coip_pool"] = aws_sdk_ec2.types.coip_pool.deserialize_ec2_query(
            child_coip_pool
        )
    return out
