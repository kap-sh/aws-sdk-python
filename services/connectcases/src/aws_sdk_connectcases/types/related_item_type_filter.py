"""Generated from Smithy shape ``com.amazonaws.connectcases#RelatedItemTypeFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.comment_filter
    import aws_sdk_connectcases.types.connect_case_filter
    import aws_sdk_connectcases.types.contact_filter
    import aws_sdk_connectcases.types.custom_filter
    import aws_sdk_connectcases.types.file_filter
    import aws_sdk_connectcases.types.sla_filter


class _RelatedItemTypeFilter_contact(TypedDict, closed=True):
    contact: "aws_sdk_connectcases.types.contact_filter.ContactFilter"


class _RelatedItemTypeFilter_comment(TypedDict, closed=True):
    comment: "aws_sdk_connectcases.types.comment_filter.CommentFilter"


class _RelatedItemTypeFilter_file(TypedDict, closed=True):
    file: "aws_sdk_connectcases.types.file_filter.FileFilter"


class _RelatedItemTypeFilter_sla(TypedDict, closed=True):
    sla: "aws_sdk_connectcases.types.sla_filter.SlaFilter"


class _RelatedItemTypeFilter_connectCase(TypedDict, closed=True):
    connectCase: "aws_sdk_connectcases.types.connect_case_filter.ConnectCaseFilter"


class _RelatedItemTypeFilter_custom(TypedDict, closed=True):
    custom: "aws_sdk_connectcases.types.custom_filter.CustomFilter"


RelatedItemTypeFilter: TypeAlias = (
    _RelatedItemTypeFilter_contact
    | _RelatedItemTypeFilter_comment
    | _RelatedItemTypeFilter_file
    | _RelatedItemTypeFilter_sla
    | _RelatedItemTypeFilter_connectCase
    | _RelatedItemTypeFilter_custom
)


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemTypeFilter) -> dict:
    if "contact" in value:
        import aws_sdk_connectcases.types.contact_filter

        return {
            "contact": aws_sdk_connectcases.types.contact_filter.serialize_json(
                value["contact"]
            )
        }
    elif "comment" in value:
        import aws_sdk_connectcases.types.comment_filter

        return {
            "comment": aws_sdk_connectcases.types.comment_filter.serialize_json(
                value["comment"]
            )
        }
    elif "file" in value:
        import aws_sdk_connectcases.types.file_filter

        return {
            "file": aws_sdk_connectcases.types.file_filter.serialize_json(value["file"])
        }
    elif "sla" in value:
        import aws_sdk_connectcases.types.sla_filter

        return {
            "sla": aws_sdk_connectcases.types.sla_filter.serialize_json(value["sla"])
        }
    elif "connectCase" in value:
        import aws_sdk_connectcases.types.connect_case_filter

        return {
            "connectCase": aws_sdk_connectcases.types.connect_case_filter.serialize_json(
                value["connectCase"]
            )
        }
    elif "custom" in value:
        import aws_sdk_connectcases.types.custom_filter

        return {
            "custom": aws_sdk_connectcases.types.custom_filter.serialize_json(
                value["custom"]
            )
        }
    else:
        raise SerializationError("RelatedItemTypeFilter: no variant present")


def deserialize_json(data: dict) -> RelatedItemTypeFilter:
    if "contact" in data:
        import aws_sdk_connectcases.types.contact_filter

        return {
            "contact": aws_sdk_connectcases.types.contact_filter.deserialize_json(
                data["contact"]
            )
        }
    elif "comment" in data:
        import aws_sdk_connectcases.types.comment_filter

        return {
            "comment": aws_sdk_connectcases.types.comment_filter.deserialize_json(
                data["comment"]
            )
        }
    elif "file" in data:
        import aws_sdk_connectcases.types.file_filter

        return {
            "file": aws_sdk_connectcases.types.file_filter.deserialize_json(
                data["file"]
            )
        }
    elif "sla" in data:
        import aws_sdk_connectcases.types.sla_filter

        return {
            "sla": aws_sdk_connectcases.types.sla_filter.deserialize_json(data["sla"])
        }
    elif "connectCase" in data:
        import aws_sdk_connectcases.types.connect_case_filter

        return {
            "connectCase": aws_sdk_connectcases.types.connect_case_filter.deserialize_json(
                data["connectCase"]
            )
        }
    elif "custom" in data:
        import aws_sdk_connectcases.types.custom_filter

        return {
            "custom": aws_sdk_connectcases.types.custom_filter.deserialize_json(
                data["custom"]
            )
        }
    else:
        raise DeserializationError("RelatedItemTypeFilter: no recognized variant key")
