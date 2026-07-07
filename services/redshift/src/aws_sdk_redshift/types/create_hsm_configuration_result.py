"""Generated from Smithy shape ``com.amazonaws.redshift#CreateHsmConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.hsm_configuration


class CreateHsmConfigurationResult(TypedDict, closed=True):
    hsm_configuration: NotRequired[
        "aws_sdk_redshift.types.hsm_configuration.HsmConfiguration"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateHsmConfigurationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "hsm_configuration" in value:
        import aws_sdk_redshift.types.hsm_configuration

        aws_sdk_redshift.types.hsm_configuration.serialize_query(
            value["hsm_configuration"], pairs, f"{prefix}.HsmConfiguration"
        )


def deserialize_query(el: Element) -> CreateHsmConfigurationResult:
    out: CreateHsmConfigurationResult = {}  # type: ignore[typeddict-item]
    child_hsm_configuration = el.find("HsmConfiguration")
    if child_hsm_configuration is not None:
        import aws_sdk_redshift.types.hsm_configuration

        out["hsm_configuration"] = (
            aws_sdk_redshift.types.hsm_configuration.deserialize_query(
                child_hsm_configuration
            )
        )
    return out
