"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyAquaOutputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.aqua_configuration


class ModifyAquaOutputMessage(TypedDict, closed=True):
    aqua_configuration: NotRequired[
        "capo_redshift.types.aqua_configuration.AquaConfiguration"
    ]
    """<p>This parameter is retired. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator). </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyAquaOutputMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "aqua_configuration" in value:
        import capo_redshift.types.aqua_configuration

        capo_redshift.types.aqua_configuration.serialize_query(
            value["aqua_configuration"], pairs, f"{key_prefix}AquaConfiguration"
        )


def deserialize_query(el: Element) -> ModifyAquaOutputMessage:
    out: ModifyAquaOutputMessage = {}  # type: ignore[typeddict-item]
    child_aqua_configuration = el.find("AquaConfiguration")
    if child_aqua_configuration is not None:
        import capo_redshift.types.aqua_configuration

        out["aqua_configuration"] = (
            capo_redshift.types.aqua_configuration.deserialize_query(
                child_aqua_configuration
            )
        )
    return out
