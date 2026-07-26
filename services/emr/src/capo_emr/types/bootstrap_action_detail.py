"""Generated from Smithy shape ``com.amazonaws.emr#BootstrapActionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.bootstrap_action_config


class BootstrapActionDetail(TypedDict, closed=True):
    bootstrap_action_config: NotRequired[
        "capo_emr.types.bootstrap_action_config.BootstrapActionConfig"
    ]
    """<p>A description of the bootstrap action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BootstrapActionDetail) -> dict:
    out: dict = {}
    if "bootstrap_action_config" in value:
        import capo_emr.types.bootstrap_action_config

        out["BootstrapActionConfig"] = (
            capo_emr.types.bootstrap_action_config.serialize_aws_json_1_1(
                value["bootstrap_action_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BootstrapActionDetail:
    out: BootstrapActionDetail = {}  # type: ignore[typeddict-item]
    if "BootstrapActionConfig" in data:
        import capo_emr.types.bootstrap_action_config

        out["bootstrap_action_config"] = (
            capo_emr.types.bootstrap_action_config.deserialize_aws_json_1_1(
                data["BootstrapActionConfig"]
            )
        )
    return out
