"""Generated from Smithy shape ``com.amazonaws.customerprofiles#IntegrationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.appflow_integration


class IntegrationConfig(TypedDict):
    appflow_integration: NotRequired[
        "aws_sdk_customer_profiles.types.appflow_integration.AppflowIntegration"
    ]
    """<p>Configuration data for <code>APPFLOW_INTEGRATION</code> workflow type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationConfig) -> dict:
    out: dict = {}
    if "appflow_integration" in value:
        import aws_sdk_customer_profiles.types.appflow_integration

        out["AppflowIntegration"] = (
            aws_sdk_customer_profiles.types.appflow_integration.serialize_json(
                value["appflow_integration"]
            )
        )
    return out


def deserialize_json(data: dict) -> IntegrationConfig:
    out: IntegrationConfig = {}  # type: ignore[typeddict-item]
    if "AppflowIntegration" in data:
        import aws_sdk_customer_profiles.types.appflow_integration

        out["appflow_integration"] = (
            aws_sdk_customer_profiles.types.appflow_integration.deserialize_json(
                data["AppflowIntegration"]
            )
        )
    return out
