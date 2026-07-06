"""Generated from Smithy shape ``com.amazonaws.shield#AttackProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_shield.types.attack_layer
    import aws_sdk_shield.types.attack_property_identifier
    import aws_sdk_shield.types.long
    import aws_sdk_shield.types.top_contributors
    import aws_sdk_shield.types.unit


class AttackProperty(TypedDict, closed=True):
    attack_layer: NotRequired["aws_sdk_shield.types.attack_layer.AttackLayer"]
    r"""<p>The type of Shield event that was observed. <code>NETWORK</code> indicates layer 3 and layer 4 events and <code>APPLICATION</code> indicates layer 7 events.</p> <p>For infrastructure layer events (L3 and L4 events), you can view metrics for top contributors in Amazon CloudWatch metrics. For more information, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html#set-ddos-alarms\">Shield metrics and alarms</a> in the <i>WAF Developer Guide</i>. </p>"""
    attack_property_identifier: NotRequired[
        "aws_sdk_shield.types.attack_property_identifier.AttackPropertyIdentifier"
    ]
    """<p>Defines the Shield event property information that is provided. The <code>WORDPRESS_PINGBACK_REFLECTOR</code> and <code>WORDPRESS_PINGBACK_SOURCE</code> values are valid only for WordPress reflective pingback events.</p>"""
    top_contributors: NotRequired[
        "aws_sdk_shield.types.top_contributors.TopContributors"
    ]
    """<p>Contributor objects for the top five contributors to a Shield event. A contributor is a source of traffic that Shield Advanced identifies as responsible for some or all of an event.</p>"""
    unit: NotRequired["aws_sdk_shield.types.unit.Unit"]
    """<p>The unit used for the <code>Contributor</code> <code>Value</code> property. </p>"""
    total: "aws_sdk_shield.types.long.Long"
    """<p>The total contributions made to this Shield event by all contributors.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackProperty) -> dict:
    out: dict = {}
    if "attack_layer" in value:
        import aws_sdk_shield.types.attack_layer

        out["AttackLayer"] = aws_sdk_shield.types.attack_layer.serialize_aws_json_1_1(
            value["attack_layer"]
        )
    if "attack_property_identifier" in value:
        import aws_sdk_shield.types.attack_property_identifier

        out["AttackPropertyIdentifier"] = (
            aws_sdk_shield.types.attack_property_identifier.serialize_aws_json_1_1(
                value["attack_property_identifier"]
            )
        )
    if "top_contributors" in value:
        import aws_sdk_shield.types.top_contributors

        out["TopContributors"] = (
            aws_sdk_shield.types.top_contributors.serialize_aws_json_1_1(
                value["top_contributors"]
            )
        )
    if "unit" in value:
        import aws_sdk_shield.types.unit

        out["Unit"] = aws_sdk_shield.types.unit.serialize_aws_json_1_1(value["unit"])
    out["Total"] = value.get("total", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> AttackProperty:
    out: AttackProperty = {}  # type: ignore[typeddict-item]
    if "AttackLayer" in data:
        import aws_sdk_shield.types.attack_layer

        out["attack_layer"] = (
            aws_sdk_shield.types.attack_layer.deserialize_aws_json_1_1(
                data["AttackLayer"]
            )
        )
    if "AttackPropertyIdentifier" in data:
        import aws_sdk_shield.types.attack_property_identifier

        out["attack_property_identifier"] = (
            aws_sdk_shield.types.attack_property_identifier.deserialize_aws_json_1_1(
                data["AttackPropertyIdentifier"]
            )
        )
    if "TopContributors" in data:
        import aws_sdk_shield.types.top_contributors

        out["top_contributors"] = (
            aws_sdk_shield.types.top_contributors.deserialize_aws_json_1_1(
                data["TopContributors"]
            )
        )
    if "Unit" in data:
        import aws_sdk_shield.types.unit

        out["unit"] = aws_sdk_shield.types.unit.deserialize_aws_json_1_1(data["Unit"])
    if "Total" in data:
        out["total"] = data["Total"]
    else:
        out["total"] = 0
    return out
