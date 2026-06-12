"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyAquaOutputMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.aqua_configuration


class ModifyAquaOutputMessage(TypedDict):
    aqua_configuration: NotRequired[
        "aws_sdk_redshift.types.aqua_configuration.AquaConfiguration"
    ]
    """<p>This parameter is retired. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator). </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyAquaOutputMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "aqua_configuration" in value:
        import aws_sdk_redshift.types.aqua_configuration

        aws_sdk_redshift.types.aqua_configuration.serialize_query(
            value["aqua_configuration"], pairs, f"{prefix}.AquaConfiguration"
        )


def deserialize_query(el: Element) -> ModifyAquaOutputMessage:
    out: ModifyAquaOutputMessage = {}  # type: ignore[typeddict-item]
    child_aqua_configuration = el.find("AquaConfiguration")
    if child_aqua_configuration is not None:
        import aws_sdk_redshift.types.aqua_configuration

        out["aqua_configuration"] = (
            aws_sdk_redshift.types.aqua_configuration.deserialize_query(
                child_aqua_configuration
            )
        )
    return out
