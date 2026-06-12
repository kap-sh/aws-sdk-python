"""Generated from Smithy shape ``com.amazonaws.health#EventTypeFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_health.types.event_type_actionability_list
    import aws_sdk_health.types.event_type_category_list
    import aws_sdk_health.types.event_type_code_list
    import aws_sdk_health.types.event_type_persona_list
    import aws_sdk_health.types.service_list


class EventTypeFilter(TypedDict):
    event_type_codes: NotRequired[
        "aws_sdk_health.types.event_type_code_list.EventTypeCodeList"
    ]
    """<p>A list of event type codes.</p>"""
    services: NotRequired["aws_sdk_health.types.service_list.serviceList"]
    """<p>The Amazon Web Services services associated with the event. For example, <code>EC2</code>, <code>RDS</code>.</p>"""
    event_type_categories: NotRequired[
        "aws_sdk_health.types.event_type_category_list.EventTypeCategoryList"
    ]
    """<p>A list of event type category codes. Possible values are <code>issue</code>, <code>accountNotification</code>, or <code>scheduledChange</code>. Currently, the <code>investigation</code> value isn't supported at this time.</p>"""
    actionabilities: NotRequired[
        "aws_sdk_health.types.event_type_actionability_list.EventTypeActionabilityList"
    ]
    """<p>A list of actionability values to filter event types. Possible values are <code>ACTION_REQUIRED</code>, <code>ACTION_MAY_BE_REQUIRED</code> and <code>INFORMATIONAL</code>.</p>"""
    personas: NotRequired[
        "aws_sdk_health.types.event_type_persona_list.EventTypePersonaList"
    ]
    """<p>A list of persona classifications to filter event types. Possible values are <code>OPERATIONS</code>, <code>SECURITY</code>, and <code>BILLING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTypeFilter) -> dict:
    out: dict = {}
    if "event_type_codes" in value:
        import aws_sdk_health.types.event_type_code_list

        out["eventTypeCodes"] = (
            aws_sdk_health.types.event_type_code_list.serialize_aws_json_1_1(
                value["event_type_codes"]
            )
        )
    if "services" in value:
        import aws_sdk_health.types.service_list

        out["services"] = aws_sdk_health.types.service_list.serialize_aws_json_1_1(
            value["services"]
        )
    if "event_type_categories" in value:
        import aws_sdk_health.types.event_type_category_list

        out["eventTypeCategories"] = (
            aws_sdk_health.types.event_type_category_list.serialize_aws_json_1_1(
                value["event_type_categories"]
            )
        )
    if "actionabilities" in value:
        import aws_sdk_health.types.event_type_actionability_list

        out["actionabilities"] = (
            aws_sdk_health.types.event_type_actionability_list.serialize_aws_json_1_1(
                value["actionabilities"]
            )
        )
    if "personas" in value:
        import aws_sdk_health.types.event_type_persona_list

        out["personas"] = (
            aws_sdk_health.types.event_type_persona_list.serialize_aws_json_1_1(
                value["personas"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventTypeFilter:
    out: EventTypeFilter = {}  # type: ignore[typeddict-item]
    if "eventTypeCodes" in data:
        import aws_sdk_health.types.event_type_code_list

        out["event_type_codes"] = (
            aws_sdk_health.types.event_type_code_list.deserialize_aws_json_1_1(
                data["eventTypeCodes"]
            )
        )
    if "services" in data:
        import aws_sdk_health.types.service_list

        out["services"] = aws_sdk_health.types.service_list.deserialize_aws_json_1_1(
            data["services"]
        )
    if "eventTypeCategories" in data:
        import aws_sdk_health.types.event_type_category_list

        out["event_type_categories"] = (
            aws_sdk_health.types.event_type_category_list.deserialize_aws_json_1_1(
                data["eventTypeCategories"]
            )
        )
    if "actionabilities" in data:
        import aws_sdk_health.types.event_type_actionability_list

        out["actionabilities"] = (
            aws_sdk_health.types.event_type_actionability_list.deserialize_aws_json_1_1(
                data["actionabilities"]
            )
        )
    if "personas" in data:
        import aws_sdk_health.types.event_type_persona_list

        out["personas"] = (
            aws_sdk_health.types.event_type_persona_list.deserialize_aws_json_1_1(
                data["personas"]
            )
        )
    return out
