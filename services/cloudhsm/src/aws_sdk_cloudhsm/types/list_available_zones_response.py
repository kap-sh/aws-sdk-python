"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ListAvailableZonesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.az_list


class ListAvailableZonesResponse(TypedDict, closed=True):
    az_list: NotRequired["aws_sdk_cloudhsm.types.az_list.AZList"]
    """<p>The list of Availability Zones that have available AWS CloudHSM capacity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAvailableZonesResponse) -> dict:
    out: dict = {}
    if "az_list" in value:
        import aws_sdk_cloudhsm.types.az_list

        out["AZList"] = aws_sdk_cloudhsm.types.az_list.serialize_aws_json_1_1(
            value["az_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAvailableZonesResponse:
    out: ListAvailableZonesResponse = {}  # type: ignore[typeddict-item]
    if "AZList" in data:
        import aws_sdk_cloudhsm.types.az_list

        out["az_list"] = aws_sdk_cloudhsm.types.az_list.deserialize_aws_json_1_1(
            data["AZList"]
        )
    return out
