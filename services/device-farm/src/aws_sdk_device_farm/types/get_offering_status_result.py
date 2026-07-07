"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetOfferingStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.offering_status_map
    import aws_sdk_device_farm.types.pagination_token


class GetOfferingStatusResult(TypedDict, closed=True):
    current: NotRequired[
        "aws_sdk_device_farm.types.offering_status_map.OfferingStatusMap"
    ]
    """<p>When specified, gets the offering status for the current period.</p>"""
    next_period: NotRequired[
        "aws_sdk_device_farm.types.offering_status_map.OfferingStatusMap"
    ]
    """<p>When specified, gets the offering status for the next period.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOfferingStatusResult) -> dict:
    out: dict = {}
    if "current" in value:
        import aws_sdk_device_farm.types.offering_status_map

        out["current"] = (
            aws_sdk_device_farm.types.offering_status_map.serialize_aws_json_1_1(
                value["current"]
            )
        )
    if "next_period" in value:
        import aws_sdk_device_farm.types.offering_status_map

        out["nextPeriod"] = (
            aws_sdk_device_farm.types.offering_status_map.serialize_aws_json_1_1(
                value["next_period"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOfferingStatusResult:
    out: GetOfferingStatusResult = {}  # type: ignore[typeddict-item]
    if "current" in data:
        import aws_sdk_device_farm.types.offering_status_map

        out["current"] = (
            aws_sdk_device_farm.types.offering_status_map.deserialize_aws_json_1_1(
                data["current"]
            )
        )
    if "nextPeriod" in data:
        import aws_sdk_device_farm.types.offering_status_map

        out["next_period"] = (
            aws_sdk_device_farm.types.offering_status_map.deserialize_aws_json_1_1(
                data["nextPeriod"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
