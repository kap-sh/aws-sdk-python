"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AppflowIntegration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.batches
    import aws_sdk_customer_profiles.types.flow_definition


class AppflowIntegration(TypedDict):
    flow_definition: "aws_sdk_customer_profiles.types.flow_definition.FlowDefinition"
    batches: NotRequired["aws_sdk_customer_profiles.types.batches.Batches"]
    """<p>Batches in workflow of type <code>APPFLOW_INTEGRATION</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppflowIntegration) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.flow_definition

    out["FlowDefinition"] = (
        aws_sdk_customer_profiles.types.flow_definition.serialize_json(
            value["flow_definition"]
        )
    )
    if "batches" in value:
        import aws_sdk_customer_profiles.types.batches

        out["Batches"] = aws_sdk_customer_profiles.types.batches.serialize_json(
            value["batches"]
        )
    return out


def deserialize_json(data: dict) -> AppflowIntegration:
    out: AppflowIntegration = {}  # type: ignore[typeddict-item]
    if "FlowDefinition" in data:
        import aws_sdk_customer_profiles.types.flow_definition

        out["flow_definition"] = (
            aws_sdk_customer_profiles.types.flow_definition.deserialize_json(
                data["FlowDefinition"]
            )
        )
    else:
        raise DeserializationError("AppflowIntegration.flow_definition required")
    if "Batches" in data:
        import aws_sdk_customer_profiles.types.batches

        out["batches"] = aws_sdk_customer_profiles.types.batches.deserialize_json(
            data["Batches"]
        )
    return out
