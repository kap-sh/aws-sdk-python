"""Generated from Smithy shape ``com.amazonaws.cloudformation#SetTypeConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.type_configuration_arn


class SetTypeConfigurationOutput(TypedDict, closed=True):
    configuration_arn: NotRequired[
        "capo_cloudformation.types.type_configuration_arn.TypeConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) for the configuration data in this account and Region.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetTypeConfigurationOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "configuration_arn" in value:
        pairs.append((f"{key_prefix}ConfigurationArn", str(value["configuration_arn"])))


def deserialize_query(el: Element) -> SetTypeConfigurationOutput:
    out: SetTypeConfigurationOutput = {}  # type: ignore[typeddict-item]
    child_configuration_arn = el.find("ConfigurationArn")
    if child_configuration_arn is not None:
        out["configuration_arn"] = str(child_configuration_arn.text or "")
    return out
