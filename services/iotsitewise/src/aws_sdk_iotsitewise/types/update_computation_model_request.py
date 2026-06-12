"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateComputationModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.computation_model_configuration
    import aws_sdk_iotsitewise.types.computation_model_data_binding
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.restricted_description
    import aws_sdk_iotsitewise.types.restricted_name


class UpdateComputationModelRequest(TypedDict):
    computation_model_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the computation model.</p>"""
    computation_model_name: "aws_sdk_iotsitewise.types.restricted_name.RestrictedName"
    """<p>The name of the computation model.</p>"""
    computation_model_description: NotRequired[
        "aws_sdk_iotsitewise.types.restricted_description.RestrictedDescription"
    ]
    """<p>The description of the computation model.</p>"""
    computation_model_configuration: "aws_sdk_iotsitewise.types.computation_model_configuration.ComputationModelConfiguration"
    """<p>The configuration for the computation model.</p>"""
    computation_model_data_binding: "aws_sdk_iotsitewise.types.computation_model_data_binding.ComputationModelDataBinding"
    """<p>The data binding for the computation model. Key is a variable name defined in configuration. Value is a <code>ComputationModelDataBindingValue</code> referenced by the variable.</p>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateComputationModelRequest) -> dict:
    out: dict = {}
    out["computationModelName"] = value["computation_model_name"]
    if "computation_model_description" in value:
        out["computationModelDescription"] = value["computation_model_description"]
    import aws_sdk_iotsitewise.types.computation_model_configuration

    out["computationModelConfiguration"] = (
        aws_sdk_iotsitewise.types.computation_model_configuration.serialize_json(
            value["computation_model_configuration"]
        )
    )
    import aws_sdk_iotsitewise.types.computation_model_data_binding

    out["computationModelDataBinding"] = (
        aws_sdk_iotsitewise.types.computation_model_data_binding.serialize_json(
            value["computation_model_data_binding"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateComputationModelRequest:
    out: UpdateComputationModelRequest = {}  # type: ignore[typeddict-item]
    if "computationModelName" in data:
        out["computation_model_name"] = data["computationModelName"]
    else:
        raise DeserializationError(
            "UpdateComputationModelRequest.computation_model_name required"
        )
    if "computationModelDescription" in data:
        out["computation_model_description"] = data["computationModelDescription"]
    if "computationModelConfiguration" in data:
        import aws_sdk_iotsitewise.types.computation_model_configuration

        out["computation_model_configuration"] = (
            aws_sdk_iotsitewise.types.computation_model_configuration.deserialize_json(
                data["computationModelConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateComputationModelRequest.computation_model_configuration required"
        )
    if "computationModelDataBinding" in data:
        import aws_sdk_iotsitewise.types.computation_model_data_binding

        out["computation_model_data_binding"] = (
            aws_sdk_iotsitewise.types.computation_model_data_binding.deserialize_json(
                data["computationModelDataBinding"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateComputationModelRequest.computation_model_data_binding required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
