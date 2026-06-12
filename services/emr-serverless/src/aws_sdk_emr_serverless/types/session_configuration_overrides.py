"""Generated from Smithy shape ``com.amazonaws.emrserverless#SessionConfigurationOverrides``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.configuration_list


class SessionConfigurationOverrides(TypedDict):
    runtime_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.configuration_list.ConfigurationList"
    ]
    """<p>The runtime configuration for the session. Contains Spark configuration properties specified at session creation time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionConfigurationOverrides) -> dict:
    out: dict = {}
    if "runtime_configuration" in value:
        import aws_sdk_emr_serverless.types.configuration_list

        out["runtimeConfiguration"] = (
            aws_sdk_emr_serverless.types.configuration_list.serialize_json(
                value["runtime_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SessionConfigurationOverrides:
    out: SessionConfigurationOverrides = {}  # type: ignore[typeddict-item]
    if "runtimeConfiguration" in data:
        import aws_sdk_emr_serverless.types.configuration_list

        out["runtime_configuration"] = (
            aws_sdk_emr_serverless.types.configuration_list.deserialize_json(
                data["runtimeConfiguration"]
            )
        )
    return out
