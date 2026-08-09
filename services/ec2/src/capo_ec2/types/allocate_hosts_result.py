"""Generated from Smithy shape ``com.amazonaws.ec2#AllocateHostsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.response_host_id_list


class AllocateHostsResult(TypedDict, closed=True):
    host_ids: NotRequired["capo_ec2.types.response_host_id_list.ResponseHostIdList"]
    """<p>The ID of the allocated Dedicated Host. This is used to launch an instance onto a specific host.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AllocateHostsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "host_ids" in value:
        import capo_ec2.types.response_host_id_list

        capo_ec2.types.response_host_id_list.serialize_ec2_query(
            value["host_ids"], pairs, f"{key_prefix}HostIdSet"
        )


def deserialize_ec2_query(el: Element) -> AllocateHostsResult:
    out: AllocateHostsResult = {}  # type: ignore[typeddict-item]
    child_host_ids = el.find("hostIdSet")
    if child_host_ids is not None:
        import capo_ec2.types.response_host_id_list

        out["host_ids"] = capo_ec2.types.response_host_id_list.deserialize_ec2_query(
            child_host_ids
        )
    return out
