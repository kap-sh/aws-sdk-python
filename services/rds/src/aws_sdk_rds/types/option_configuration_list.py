"""Generated from Smithy shape ``com.amazonaws.rds#OptionConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.option_configuration

OptionConfigurationList: TypeAlias = list[
    "aws_sdk_rds.types.option_configuration.OptionConfiguration"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.option_configuration

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.option_configuration.serialize_query(
            item, pairs, f"{prefix}.OptionConfiguration.{n}"
        )


def deserialize_query(el: Element) -> OptionConfigurationList:
    import aws_sdk_rds.types.option_configuration

    out: OptionConfigurationList = []
    for child in el.findall("OptionConfiguration"):
        out.append(aws_sdk_rds.types.option_configuration.deserialize_query(child))
    return out


def serialize_query_flat(
    value: OptionConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.option_configuration

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.option_configuration.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> OptionConfigurationList:
    import aws_sdk_rds.types.option_configuration

    out: OptionConfigurationList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.option_configuration.deserialize_query(child))
    return out
