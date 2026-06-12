"""Generated from Smithy shape ``com.amazonaws.interconnect#Bandwidths``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.bandwidth_list


class Bandwidths(TypedDict):
    available: NotRequired["aws_sdk_interconnect.types.bandwidth_list.BandwidthList"]
    """<p>The list of currently available bandwidths.</p>"""
    supported: NotRequired["aws_sdk_interconnect.types.bandwidth_list.BandwidthList"]
    """<p>The list of all bandwidths that this environment plans to support</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Bandwidths) -> dict:
    out: dict = {}
    if "available" in value:
        import aws_sdk_interconnect.types.bandwidth_list

        out["available"] = (
            aws_sdk_interconnect.types.bandwidth_list.serialize_aws_json_1_0(
                value["available"]
            )
        )
    if "supported" in value:
        import aws_sdk_interconnect.types.bandwidth_list

        out["supported"] = (
            aws_sdk_interconnect.types.bandwidth_list.serialize_aws_json_1_0(
                value["supported"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Bandwidths:
    out: Bandwidths = {}  # type: ignore[typeddict-item]
    if "available" in data:
        import aws_sdk_interconnect.types.bandwidth_list

        out["available"] = (
            aws_sdk_interconnect.types.bandwidth_list.deserialize_aws_json_1_0(
                data["available"]
            )
        )
    if "supported" in data:
        import aws_sdk_interconnect.types.bandwidth_list

        out["supported"] = (
            aws_sdk_interconnect.types.bandwidth_list.deserialize_aws_json_1_0(
                data["supported"]
            )
        )
    return out
