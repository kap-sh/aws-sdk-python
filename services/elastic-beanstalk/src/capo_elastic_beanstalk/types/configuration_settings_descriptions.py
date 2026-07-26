"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ConfigurationSettingsDescriptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.configuration_settings_description_list


class ConfigurationSettingsDescriptions(TypedDict, closed=True):
    configuration_settings: NotRequired[
        "capo_elastic_beanstalk.types.configuration_settings_description_list.ConfigurationSettingsDescriptionList"
    ]
    """<p> A list of <a>ConfigurationSettingsDescription</a>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigurationSettingsDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "configuration_settings" in value:
        import capo_elastic_beanstalk.types.configuration_settings_description_list

        capo_elastic_beanstalk.types.configuration_settings_description_list.serialize_query(
            value["configuration_settings"], pairs, f"{prefix}.ConfigurationSettings"
        )


def deserialize_query(el: Element) -> ConfigurationSettingsDescriptions:
    out: ConfigurationSettingsDescriptions = {}  # type: ignore[typeddict-item]
    child_configuration_settings = el.find("ConfigurationSettings")
    if child_configuration_settings is not None:
        import capo_elastic_beanstalk.types.configuration_settings_description_list

        out["configuration_settings"] = (
            capo_elastic_beanstalk.types.configuration_settings_description_list.deserialize_query(
                child_configuration_settings
            )
        )
    return out
