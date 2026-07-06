"""Generated from Smithy shape ``com.amazonaws.support#DescribeServicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_support.types.service_list


class DescribeServicesResponse(TypedDict, closed=True):
    services: NotRequired["aws_sdk_support.types.service_list.ServiceList"]
    """<p>A JSON-formatted list of Amazon Web Services services.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServicesResponse) -> dict:
    out: dict = {}
    if "services" in value:
        import aws_sdk_support.types.service_list

        out["services"] = aws_sdk_support.types.service_list.serialize_aws_json_1_1(
            value["services"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServicesResponse:
    out: DescribeServicesResponse = {}  # type: ignore[typeddict-item]
    if "services" in data:
        import aws_sdk_support.types.service_list

        out["services"] = aws_sdk_support.types.service_list.deserialize_aws_json_1_1(
            data["services"]
        )
    return out
