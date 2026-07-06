"""Generated from Smithy shape ``com.amazonaws.glue#Capabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.authentication_types
    import aws_sdk_glue.types.compute_environments
    import aws_sdk_glue.types.data_operations


class Capabilities(TypedDict, closed=True):
    supported_authentication_types: (
        "aws_sdk_glue.types.authentication_types.AuthenticationTypes"
    )
    """<p>A list of supported authentication types.</p>"""
    supported_data_operations: "aws_sdk_glue.types.data_operations.DataOperations"
    """<p>A list of supported data operations.</p>"""
    supported_compute_environments: (
        "aws_sdk_glue.types.compute_environments.ComputeEnvironments"
    )
    """<p>A list of supported compute environments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Capabilities) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.authentication_types

    out["SupportedAuthenticationTypes"] = (
        aws_sdk_glue.types.authentication_types.serialize_aws_json_1_1(
            value["supported_authentication_types"]
        )
    )
    import aws_sdk_glue.types.data_operations

    out["SupportedDataOperations"] = (
        aws_sdk_glue.types.data_operations.serialize_aws_json_1_1(
            value["supported_data_operations"]
        )
    )
    import aws_sdk_glue.types.compute_environments

    out["SupportedComputeEnvironments"] = (
        aws_sdk_glue.types.compute_environments.serialize_aws_json_1_1(
            value["supported_compute_environments"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Capabilities:
    out: Capabilities = {}  # type: ignore[typeddict-item]
    if "SupportedAuthenticationTypes" in data:
        import aws_sdk_glue.types.authentication_types

        out["supported_authentication_types"] = (
            aws_sdk_glue.types.authentication_types.deserialize_aws_json_1_1(
                data["SupportedAuthenticationTypes"]
            )
        )
    else:
        raise DeserializationError(
            "Capabilities.supported_authentication_types required"
        )
    if "SupportedDataOperations" in data:
        import aws_sdk_glue.types.data_operations

        out["supported_data_operations"] = (
            aws_sdk_glue.types.data_operations.deserialize_aws_json_1_1(
                data["SupportedDataOperations"]
            )
        )
    else:
        raise DeserializationError("Capabilities.supported_data_operations required")
    if "SupportedComputeEnvironments" in data:
        import aws_sdk_glue.types.compute_environments

        out["supported_compute_environments"] = (
            aws_sdk_glue.types.compute_environments.deserialize_aws_json_1_1(
                data["SupportedComputeEnvironments"]
            )
        )
    else:
        raise DeserializationError(
            "Capabilities.supported_compute_environments required"
        )
    return out
