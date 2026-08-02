"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCoipPoolResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.coip_pool


class CreateCoipPoolResult(TypedDict, closed=True):
    coip_pool: NotRequired["capo_ec2.types.coip_pool.CoipPool"]
    """<p>Information about the CoIP address pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCoipPoolResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "coip_pool" in value:
        import capo_ec2.types.coip_pool

        capo_ec2.types.coip_pool.serialize_ec2_query(
            value["coip_pool"], pairs, f"{key_prefix}CoipPool"
        )


def deserialize_ec2_query(el: Element) -> CreateCoipPoolResult:
    out: CreateCoipPoolResult = {}  # type: ignore[typeddict-item]
    child_coip_pool = el.find("CoipPool")
    if child_coip_pool is not None:
        import capo_ec2.types.coip_pool

        out["coip_pool"] = capo_ec2.types.coip_pool.deserialize_ec2_query(
            child_coip_pool
        )
    return out
