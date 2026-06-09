"""Generated from Smithy shape ``com.amazonaws.ec2#ReleaseHostsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.request_host_id_list


class ReleaseHostsRequest(TypedDict):
    host_ids: NotRequired["aws_sdk_ec2.types.request_host_id_list.RequestHostIdList"]
    """<p>The IDs of the Dedicated Hosts to release.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReleaseHostsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "host_ids" in value:
        import aws_sdk_ec2.types.request_host_id_list

        aws_sdk_ec2.types.request_host_id_list.serialize_ec2_query(
            value["host_ids"], pairs, f"{prefix}.HostId"
        )


def deserialize_ec2_query(el: Element) -> ReleaseHostsRequest:
    out: ReleaseHostsRequest = {}  # type: ignore[typeddict-item]
    if el.find("HostId") is not None:
        import aws_sdk_ec2.types.request_host_id_list

        out["host_ids"] = aws_sdk_ec2.types.request_host_id_list.deserialize_ec2_query(
            el, "HostId"
        )
    return out
