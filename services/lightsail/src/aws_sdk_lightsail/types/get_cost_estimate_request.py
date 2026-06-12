"""Generated from Smithy shape ``com.amazonaws.lightsail#GetCostEstimateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.resource_name


class GetCostEstimateRequest(TypedDict):
    resource_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The resource name.</p>"""
    start_time: "aws_sdk_lightsail.types.iso_date.IsoDate"
    """<p>The cost estimate start time.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you want to use a start time of October 1, 2018, at 8 PM UTC, specify <code>1538424000</code> as the start time.</p> </li> </ul> <p>You can convert a human-friendly time to Unix time format using a converter like <a href=\"https://www.epochconverter.com/\">Epoch converter</a>.</p>"""
    end_time: "aws_sdk_lightsail.types.iso_date.IsoDate"
    """<p>The cost estimate end time.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you want to use an end time of October 1, 2018, at 9 PM UTC, specify <code>1538427600</code> as the end time.</p> </li> </ul> <p>You can convert a human-friendly time to Unix time format using a converter like <a href=\"https://www.epochconverter.com/\">Epoch converter</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCostEstimateRequest) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    import aws_sdk_lightsail.types.iso_date

    out["startTime"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
        value["start_time"]
    )
    import aws_sdk_lightsail.types.iso_date

    out["endTime"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
        value["end_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCostEstimateRequest:
    out: GetCostEstimateRequest = {}  # type: ignore[typeddict-item]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    else:
        raise DeserializationError("GetCostEstimateRequest.resource_name required")
    if "startTime" in data:
        import aws_sdk_lightsail.types.iso_date

        out["start_time"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["startTime"]
        )
    else:
        raise DeserializationError("GetCostEstimateRequest.start_time required")
    if "endTime" in data:
        import aws_sdk_lightsail.types.iso_date

        out["end_time"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["endTime"]
        )
    else:
        raise DeserializationError("GetCostEstimateRequest.end_time required")
    return out
