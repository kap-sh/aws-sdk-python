"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.describe_configurations_attributes


class DescribeConfigurationsResponse(TypedDict, closed=True):
    configurations: NotRequired[
        "capo_application_discovery_service.types.describe_configurations_attributes.DescribeConfigurationsAttributes"
    ]
    """<p>A key in the response map. The value is an array of data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigurationsResponse) -> dict:
    out: dict = {}
    if "configurations" in value:
        import capo_application_discovery_service.types.describe_configurations_attributes

        out["configurations"] = (
            capo_application_discovery_service.types.describe_configurations_attributes.serialize_aws_json_1_1(
                value["configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigurationsResponse:
    out: DescribeConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "configurations" in data:
        import capo_application_discovery_service.types.describe_configurations_attributes

        out["configurations"] = (
            capo_application_discovery_service.types.describe_configurations_attributes.deserialize_aws_json_1_1(
                data["configurations"]
            )
        )
    return out
