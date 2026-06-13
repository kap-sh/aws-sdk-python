"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetMLEndpointOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.ml_config_definition
    import aws_sdk_neptunedata.types.ml_resource_definition


class GetMLEndpointOutput(TypedDict):
    status: NotRequired["str"]
    """<p>The status of the inference endpoint.</p>"""
    id: NotRequired["str"]
    """<p>The unique identifier of the inference endpoint.</p>"""
    endpoint: NotRequired[
        "aws_sdk_neptunedata.types.ml_resource_definition.MlResourceDefinition"
    ]
    """<p>The endpoint definition.</p>"""
    endpoint_config: NotRequired[
        "aws_sdk_neptunedata.types.ml_config_definition.MlConfigDefinition"
    ]
    """<p>The endpoint configuration</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMLEndpointOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "id" in value:
        out["id"] = value["id"]
    if "endpoint" in value:
        import aws_sdk_neptunedata.types.ml_resource_definition

        out["endpoint"] = (
            aws_sdk_neptunedata.types.ml_resource_definition.serialize_json(
                value["endpoint"]
            )
        )
    if "endpoint_config" in value:
        import aws_sdk_neptunedata.types.ml_config_definition

        out["endpointConfig"] = (
            aws_sdk_neptunedata.types.ml_config_definition.serialize_json(
                value["endpoint_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMLEndpointOutput:
    out: GetMLEndpointOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "id" in data:
        out["id"] = data["id"]
    if "endpoint" in data:
        import aws_sdk_neptunedata.types.ml_resource_definition

        out["endpoint"] = (
            aws_sdk_neptunedata.types.ml_resource_definition.deserialize_json(
                data["endpoint"]
            )
        )
    if "endpointConfig" in data:
        import aws_sdk_neptunedata.types.ml_config_definition

        out["endpoint_config"] = (
            aws_sdk_neptunedata.types.ml_config_definition.deserialize_json(
                data["endpointConfig"]
            )
        )
    return out
