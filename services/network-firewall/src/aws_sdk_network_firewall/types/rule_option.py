"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.keyword
    import aws_sdk_network_firewall.types.settings


class RuleOption(TypedDict):
    keyword: "aws_sdk_network_firewall.types.keyword.Keyword"
    r"""<p>The keyword for the Suricata compatible rule option. You must include a <code>sid</code> (signature ID), and can optionally include other keywords. For information about Suricata compatible keywords, see <a href=\"https://suricata.readthedocs.io/en/suricata-7.0.3/rules/intro.html#rule-options\">Rule options</a> in the Suricata documentation.</p>"""
    settings: NotRequired["aws_sdk_network_firewall.types.settings.Settings"]
    r"""<p>The settings of the Suricata compatible rule option. Rule options have zero or more setting values, and the number of possible and required settings depends on the <code>Keyword</code>. For more information about the settings for specific options, see <a href=\"https://suricata.readthedocs.io/en/suricata-7.0.3/rules/intro.html#rule-options\">Rule options</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleOption) -> dict:
    out: dict = {}
    out["Keyword"] = value["keyword"]
    if "settings" in value:
        import aws_sdk_network_firewall.types.settings

        out["Settings"] = (
            aws_sdk_network_firewall.types.settings.serialize_aws_json_1_0(
                value["settings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleOption:
    out: RuleOption = {}  # type: ignore[typeddict-item]
    if "Keyword" in data:
        out["keyword"] = data["Keyword"]
    else:
        raise DeserializationError("RuleOption.keyword required")
    if "Settings" in data:
        import aws_sdk_network_firewall.types.settings

        out["settings"] = (
            aws_sdk_network_firewall.types.settings.deserialize_aws_json_1_0(
                data["Settings"]
            )
        )
    return out
