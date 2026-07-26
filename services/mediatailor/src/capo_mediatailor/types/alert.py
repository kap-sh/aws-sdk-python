"""Generated from Smithy shape ``com.amazonaws.mediatailor#Alert``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__list_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.__timestamp_unix
    import capo_mediatailor.types.alert_category


class Alert(TypedDict, closed=True):
    alert_code: "capo_mediatailor.types.__string.__string"
    """<p>The code for the alert. For example, <code>NOT_PROCESSED</code>.</p>"""
    alert_message: "capo_mediatailor.types.__string.__string"
    """<p>If an alert is generated for a resource, an explanation of the reason for the alert.</p>"""
    last_modified_time: "capo_mediatailor.types.__timestamp_unix.__timestampUnix"
    """<p>The timestamp when the alert was last modified.</p>"""
    related_resource_arns: "capo_mediatailor.types.__list_of__string.__listOf__string"
    """<p>The Amazon Resource Names (ARNs) related to this alert.</p>"""
    resource_arn: "capo_mediatailor.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    category: NotRequired["capo_mediatailor.types.alert_category.AlertCategory"]
    """<p>The category that MediaTailor assigns to the alert.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Alert) -> dict:
    out: dict = {}
    out["AlertCode"] = value["alert_code"]
    out["AlertMessage"] = value["alert_message"]
    import capo_mediatailor.types.__timestamp_unix

    out["LastModifiedTime"] = capo_mediatailor.types.__timestamp_unix.serialize_json(
        value["last_modified_time"]
    )
    import capo_mediatailor.types.__list_of__string

    out["RelatedResourceArns"] = (
        capo_mediatailor.types.__list_of__string.serialize_json(
            value["related_resource_arns"]
        )
    )
    out["ResourceArn"] = value["resource_arn"]
    if "category" in value:
        import capo_mediatailor.types.alert_category

        out["Category"] = capo_mediatailor.types.alert_category.serialize_json(
            value["category"]
        )
    return out


def deserialize_json(data: dict) -> Alert:
    out: Alert = {}  # type: ignore[typeddict-item]
    if "AlertCode" in data:
        out["alert_code"] = data["AlertCode"]
    else:
        raise DeserializationError("Alert.alert_code required")
    if "AlertMessage" in data:
        out["alert_message"] = data["AlertMessage"]
    else:
        raise DeserializationError("Alert.alert_message required")
    if "LastModifiedTime" in data:
        import capo_mediatailor.types.__timestamp_unix

        out["last_modified_time"] = (
            capo_mediatailor.types.__timestamp_unix.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("Alert.last_modified_time required")
    if "RelatedResourceArns" in data:
        import capo_mediatailor.types.__list_of__string

        out["related_resource_arns"] = (
            capo_mediatailor.types.__list_of__string.deserialize_json(
                data["RelatedResourceArns"]
            )
        )
    else:
        raise DeserializationError("Alert.related_resource_arns required")
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("Alert.resource_arn required")
    if "Category" in data:
        import capo_mediatailor.types.alert_category

        out["category"] = capo_mediatailor.types.alert_category.deserialize_json(
            data["Category"]
        )
    return out
