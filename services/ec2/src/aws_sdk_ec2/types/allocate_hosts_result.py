"""Generated from Smithy shape ``com.amazonaws.ec2#AllocateHostsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.response_host_id_list


class AllocateHostsResult(TypedDict):
    host_ids: NotRequired["aws_sdk_ec2.types.response_host_id_list.ResponseHostIdList"]
    """<p>The ID of the allocated Dedicated Host. This is used to launch an instance onto a specific host.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AllocateHostsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "host_ids" in value:
        import aws_sdk_ec2.types.response_host_id_list

        aws_sdk_ec2.types.response_host_id_list.serialize_ec2_query(
            value["host_ids"], pairs, f"{prefix}.HostIdSet"
        )


def deserialize_ec2_query(el: Element) -> AllocateHostsResult:
    out: AllocateHostsResult = {}  # type: ignore[typeddict-item]
    if el.find("HostIdSet") is not None:
        import aws_sdk_ec2.types.response_host_id_list

        out["host_ids"] = aws_sdk_ec2.types.response_host_id_list.deserialize_ec2_query(
            el, "HostIdSet"
        )
    return out
