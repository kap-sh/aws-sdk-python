"""Generated from Smithy shape ``com.amazonaws.shield#AttackDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_shield.types.attack_id
    import aws_sdk_shield.types.attack_properties
    import aws_sdk_shield.types.attack_timestamp
    import aws_sdk_shield.types.mitigation_list
    import aws_sdk_shield.types.resource_arn
    import aws_sdk_shield.types.sub_resource_summary_list
    import aws_sdk_shield.types.summarized_counter_list


class AttackDetail(TypedDict, closed=True):
    attack_id: NotRequired["aws_sdk_shield.types.attack_id.AttackId"]
    """<p>The unique identifier (ID) of the attack.</p>"""
    resource_arn: NotRequired["aws_sdk_shield.types.resource_arn.ResourceArn"]
    """<p>The ARN (Amazon Resource Name) of the resource that was attacked.</p>"""
    sub_resources: NotRequired[
        "aws_sdk_shield.types.sub_resource_summary_list.SubResourceSummaryList"
    ]
    """<p>If applicable, additional detail about the resource being attacked, for example, IP address or URL.</p>"""
    start_time: NotRequired["aws_sdk_shield.types.attack_timestamp.AttackTimestamp"]
    """<p>The time the attack started, in Unix time in seconds. </p>"""
    end_time: NotRequired["aws_sdk_shield.types.attack_timestamp.AttackTimestamp"]
    """<p>The time the attack ended, in Unix time in seconds. </p>"""
    attack_counters: NotRequired[
        "aws_sdk_shield.types.summarized_counter_list.SummarizedCounterList"
    ]
    """<p>List of counters that describe the attack for the specified time period.</p>"""
    attack_properties: NotRequired[
        "aws_sdk_shield.types.attack_properties.AttackProperties"
    ]
    r"""<p>The array of objects that provide details of the Shield event. </p> <p>For infrastructure layer events (L3 and L4 events), you can view metrics for top contributors in Amazon CloudWatch metrics. For more information, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html#set-ddos-alarms\">Shield metrics and alarms</a> in the <i>WAF Developer Guide</i>. </p>"""
    mitigations: NotRequired["aws_sdk_shield.types.mitigation_list.MitigationList"]
    """<p>List of mitigation actions taken for the attack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackDetail) -> dict:
    out: dict = {}
    if "attack_id" in value:
        out["AttackId"] = value["attack_id"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "sub_resources" in value:
        import aws_sdk_shield.types.sub_resource_summary_list

        out["SubResources"] = (
            aws_sdk_shield.types.sub_resource_summary_list.serialize_aws_json_1_1(
                value["sub_resources"]
            )
        )
    if "start_time" in value:
        import aws_sdk_shield.types.attack_timestamp

        out["StartTime"] = aws_sdk_shield.types.attack_timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_shield.types.attack_timestamp

        out["EndTime"] = aws_sdk_shield.types.attack_timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "attack_counters" in value:
        import aws_sdk_shield.types.summarized_counter_list

        out["AttackCounters"] = (
            aws_sdk_shield.types.summarized_counter_list.serialize_aws_json_1_1(
                value["attack_counters"]
            )
        )
    if "attack_properties" in value:
        import aws_sdk_shield.types.attack_properties

        out["AttackProperties"] = (
            aws_sdk_shield.types.attack_properties.serialize_aws_json_1_1(
                value["attack_properties"]
            )
        )
    if "mitigations" in value:
        import aws_sdk_shield.types.mitigation_list

        out["Mitigations"] = (
            aws_sdk_shield.types.mitigation_list.serialize_aws_json_1_1(
                value["mitigations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AttackDetail:
    out: AttackDetail = {}  # type: ignore[typeddict-item]
    if "AttackId" in data:
        out["attack_id"] = data["AttackId"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "SubResources" in data:
        import aws_sdk_shield.types.sub_resource_summary_list

        out["sub_resources"] = (
            aws_sdk_shield.types.sub_resource_summary_list.deserialize_aws_json_1_1(
                data["SubResources"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_shield.types.attack_timestamp

        out["start_time"] = (
            aws_sdk_shield.types.attack_timestamp.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_shield.types.attack_timestamp

        out["end_time"] = (
            aws_sdk_shield.types.attack_timestamp.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    if "AttackCounters" in data:
        import aws_sdk_shield.types.summarized_counter_list

        out["attack_counters"] = (
            aws_sdk_shield.types.summarized_counter_list.deserialize_aws_json_1_1(
                data["AttackCounters"]
            )
        )
    if "AttackProperties" in data:
        import aws_sdk_shield.types.attack_properties

        out["attack_properties"] = (
            aws_sdk_shield.types.attack_properties.deserialize_aws_json_1_1(
                data["AttackProperties"]
            )
        )
    if "Mitigations" in data:
        import aws_sdk_shield.types.mitigation_list

        out["mitigations"] = (
            aws_sdk_shield.types.mitigation_list.deserialize_aws_json_1_1(
                data["Mitigations"]
            )
        )
    return out
