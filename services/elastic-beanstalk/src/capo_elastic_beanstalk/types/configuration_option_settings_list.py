"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ConfigurationOptionSettingsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.configuration_option_setting

ConfigurationOptionSettingsList: TypeAlias = list[
    "capo_elastic_beanstalk.types.configuration_option_setting.ConfigurationOptionSetting"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigurationOptionSettingsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.configuration_option_setting

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.configuration_option_setting.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ConfigurationOptionSettingsList:
    import capo_elastic_beanstalk.types.configuration_option_setting

    out: ConfigurationOptionSettingsList = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_beanstalk.types.configuration_option_setting.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ConfigurationOptionSettingsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.configuration_option_setting

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.configuration_option_setting.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> ConfigurationOptionSettingsList:
    import capo_elastic_beanstalk.types.configuration_option_setting

    out: ConfigurationOptionSettingsList = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_beanstalk.types.configuration_option_setting.deserialize_query(
                child
            )
        )
    return out
