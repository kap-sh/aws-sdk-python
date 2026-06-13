"""Generated from Smithy shape ``com.amazonaws.mailmanager#StartArchiveSearchRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mailmanager.types.archive_filters
    import aws_sdk_mailmanager.types.archive_id
    import aws_sdk_mailmanager.types.search_max_results


class StartArchiveSearchRequest(TypedDict):
    archive_id: "aws_sdk_mailmanager.types.archive_id.ArchiveId"
    """<p>The identifier of the archive to search emails in.</p>"""
    filters: NotRequired["aws_sdk_mailmanager.types.archive_filters.ArchiveFilters"]
    """<p>Criteria to filter which emails are included in the search results.</p>"""
    from_timestamp: "datetime.datetime"
    """<p>The start timestamp of the range to search emails from.</p>"""
    to_timestamp: "datetime.datetime"
    """<p>The end timestamp of the range to search emails from.</p>"""
    max_results: "aws_sdk_mailmanager.types.search_max_results.SearchMaxResults"
    """<p>The maximum number of search results to return.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartArchiveSearchRequest) -> dict:
    out: dict = {}
    out["ArchiveId"] = value["archive_id"]
    if "filters" in value:
        import aws_sdk_mailmanager.types.archive_filters

        out["Filters"] = (
            aws_sdk_mailmanager.types.archive_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    import aws_sdk_mailmanager.types._prelude.timestamp

    out["FromTimestamp"] = (
        aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["from_timestamp"]
        )
    )
    import aws_sdk_mailmanager.types._prelude.timestamp

    out["ToTimestamp"] = (
        aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["to_timestamp"]
        )
    )
    out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartArchiveSearchRequest:
    out: StartArchiveSearchRequest = {}  # type: ignore[typeddict-item]
    if "ArchiveId" in data:
        out["archive_id"] = data["ArchiveId"]
    else:
        raise DeserializationError("StartArchiveSearchRequest.archive_id required")
    if "Filters" in data:
        import aws_sdk_mailmanager.types.archive_filters

        out["filters"] = (
            aws_sdk_mailmanager.types.archive_filters.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if "FromTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["from_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["FromTimestamp"]
            )
        )
    else:
        raise DeserializationError("StartArchiveSearchRequest.from_timestamp required")
    if "ToTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["to_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["ToTimestamp"]
            )
        )
    else:
        raise DeserializationError("StartArchiveSearchRequest.to_timestamp required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        raise DeserializationError("StartArchiveSearchRequest.max_results required")
    return out
