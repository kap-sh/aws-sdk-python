"""Generated from Smithy shape ``com.amazonaws.redshift#AquaConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.aqua_configuration_status
    import aws_sdk_redshift.types.aqua_status


class AquaConfiguration(TypedDict):
    aqua_status: NotRequired["aws_sdk_redshift.types.aqua_status.AquaStatus"]
    """<p>This field is retired. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).</p>"""
    aqua_configuration_status: NotRequired[
        "aws_sdk_redshift.types.aqua_configuration_status.AquaConfigurationStatus"
    ]
    """<p>This field is retired. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AquaConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "aqua_status" in value:
        import aws_sdk_redshift.types.aqua_status

        aws_sdk_redshift.types.aqua_status.serialize_query(
            value["aqua_status"], pairs, f"{prefix}.AquaStatus"
        )
    if "aqua_configuration_status" in value:
        import aws_sdk_redshift.types.aqua_configuration_status

        aws_sdk_redshift.types.aqua_configuration_status.serialize_query(
            value["aqua_configuration_status"],
            pairs,
            f"{prefix}.AquaConfigurationStatus",
        )


def deserialize_query(el: Element) -> AquaConfiguration:
    out: AquaConfiguration = {}  # type: ignore[typeddict-item]
    child_aqua_status = el.find("AquaStatus")
    if child_aqua_status is not None:
        import aws_sdk_redshift.types.aqua_status

        out["aqua_status"] = aws_sdk_redshift.types.aqua_status.deserialize_query(
            child_aqua_status
        )
    child_aqua_configuration_status = el.find("AquaConfigurationStatus")
    if child_aqua_configuration_status is not None:
        import aws_sdk_redshift.types.aqua_configuration_status

        out["aqua_configuration_status"] = (
            aws_sdk_redshift.types.aqua_configuration_status.deserialize_query(
                child_aqua_configuration_status
            )
        )
    return out
