"""Generated from Smithy shape ``com.amazonaws.redshift#HsmConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.hsm_configuration

HsmConfigurationList: TypeAlias = list[
    "aws_sdk_redshift.types.hsm_configuration.HsmConfiguration"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: HsmConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.hsm_configuration

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.hsm_configuration.serialize_query(
            item, pairs, f"{prefix}.HsmConfiguration.{n}"
        )


def deserialize_query(el: Element) -> HsmConfigurationList:
    import aws_sdk_redshift.types.hsm_configuration

    out: HsmConfigurationList = []
    for child in el.findall("HsmConfiguration"):
        out.append(aws_sdk_redshift.types.hsm_configuration.deserialize_query(child))
    return out


def serialize_query_flat(
    value: HsmConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.hsm_configuration

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.hsm_configuration.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> HsmConfigurationList:
    import aws_sdk_redshift.types.hsm_configuration

    out: HsmConfigurationList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.hsm_configuration.deserialize_query(child))
    return out
