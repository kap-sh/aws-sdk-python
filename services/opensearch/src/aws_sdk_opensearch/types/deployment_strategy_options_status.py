"""Generated from Smithy shape ``com.amazonaws.opensearch#DeploymentStrategyOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.deployment_strategy_options
    import aws_sdk_opensearch.types.option_status


class DeploymentStrategyOptionsStatus(TypedDict, closed=True):
    options: (
        "aws_sdk_opensearch.types.deployment_strategy_options.DeploymentStrategyOptions"
    )
    """<p>Deployment strategy options for the domain.</p>"""
    status: "aws_sdk_opensearch.types.option_status.OptionStatus"
    """<p>The current status of the deployment strategy options for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStrategyOptionsStatus) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.deployment_strategy_options

    out["Options"] = (
        aws_sdk_opensearch.types.deployment_strategy_options.serialize_json(
            value["options"]
        )
    )
    import aws_sdk_opensearch.types.option_status

    out["Status"] = aws_sdk_opensearch.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeploymentStrategyOptionsStatus:
    out: DeploymentStrategyOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_opensearch.types.deployment_strategy_options

        out["options"] = (
            aws_sdk_opensearch.types.deployment_strategy_options.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError("DeploymentStrategyOptionsStatus.options required")
    if "Status" in data:
        import aws_sdk_opensearch.types.option_status

        out["status"] = aws_sdk_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("DeploymentStrategyOptionsStatus.status required")
    return out
