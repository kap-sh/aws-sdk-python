"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DeploymentStrategyOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.deployment_strategy_options
    import capo_elasticsearch_service.types.option_status


class DeploymentStrategyOptionsStatus(TypedDict, closed=True):
    options: "capo_elasticsearch_service.types.deployment_strategy_options.DeploymentStrategyOptions"
    """<p>Specifies deployment strategy options for the specified Elasticsearch domain.</p>"""
    status: "capo_elasticsearch_service.types.option_status.OptionStatus"
    """<p>Specifies the status of the deployment strategy options for the specified Elasticsearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStrategyOptionsStatus) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.deployment_strategy_options

    out["Options"] = (
        capo_elasticsearch_service.types.deployment_strategy_options.serialize_json(
            value["options"]
        )
    )
    import capo_elasticsearch_service.types.option_status

    out["Status"] = capo_elasticsearch_service.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeploymentStrategyOptionsStatus:
    out: DeploymentStrategyOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import capo_elasticsearch_service.types.deployment_strategy_options

        out["options"] = (
            capo_elasticsearch_service.types.deployment_strategy_options.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError("DeploymentStrategyOptionsStatus.options required")
    if "Status" in data:
        import capo_elasticsearch_service.types.option_status

        out["status"] = capo_elasticsearch_service.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("DeploymentStrategyOptionsStatus.status required")
    return out
