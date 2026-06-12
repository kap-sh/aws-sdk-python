"""Generated from Smithy shape ``com.amazonaws.rds#OptionGroupOptionSettingsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.option_group_option_setting

OptionGroupOptionSettingsList: TypeAlias = list[
    "aws_sdk_rds.types.option_group_option_setting.OptionGroupOptionSetting"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionGroupOptionSettingsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.option_group_option_setting

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.option_group_option_setting.serialize_query(
            item, pairs, f"{prefix}.OptionGroupOptionSetting.{n}"
        )


def deserialize_query(el: Element) -> OptionGroupOptionSettingsList:
    import aws_sdk_rds.types.option_group_option_setting

    out: OptionGroupOptionSettingsList = []
    for child in el.findall("OptionGroupOptionSetting"):
        out.append(
            aws_sdk_rds.types.option_group_option_setting.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: OptionGroupOptionSettingsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.option_group_option_setting

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.option_group_option_setting.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> OptionGroupOptionSettingsList:
    import aws_sdk_rds.types.option_group_option_setting

    out: OptionGroupOptionSettingsList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_rds.types.option_group_option_setting.deserialize_query(child)
        )
    return out
