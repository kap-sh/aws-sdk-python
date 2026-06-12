"""Generated from Smithy shape ``com.amazonaws.rds#OptionSettingConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.option_setting

OptionSettingConfigurationList: TypeAlias = list[
    "aws_sdk_rds.types.option_setting.OptionSetting"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionSettingConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.option_setting

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.option_setting.serialize_query(
            item, pairs, f"{prefix}.OptionSetting.{n}"
        )


def deserialize_query(el: Element) -> OptionSettingConfigurationList:
    import aws_sdk_rds.types.option_setting

    out: OptionSettingConfigurationList = []
    for child in el.findall("OptionSetting"):
        out.append(aws_sdk_rds.types.option_setting.deserialize_query(child))
    return out


def serialize_query_flat(
    value: OptionSettingConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.option_setting

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.option_setting.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> OptionSettingConfigurationList:
    import aws_sdk_rds.types.option_setting

    out: OptionSettingConfigurationList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.option_setting.deserialize_query(child))
    return out
