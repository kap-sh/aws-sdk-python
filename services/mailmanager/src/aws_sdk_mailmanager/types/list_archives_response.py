"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListArchivesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.archives_list
    import aws_sdk_mailmanager.types.pagination_token


class ListArchivesResponse(TypedDict):
    archives: "aws_sdk_mailmanager.types.archives_list.ArchivesList"
    """<p>The list of archive details.</p>"""
    next_token: NotRequired[
        "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
    ]
    """<p>If present, use to retrieve the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListArchivesResponse) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.archives_list

    out["Archives"] = aws_sdk_mailmanager.types.archives_list.serialize_aws_json_1_0(
        value["archives"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListArchivesResponse:
    out: ListArchivesResponse = {}  # type: ignore[typeddict-item]
    if "Archives" in data:
        import aws_sdk_mailmanager.types.archives_list

        out["archives"] = (
            aws_sdk_mailmanager.types.archives_list.deserialize_aws_json_1_0(
                data["Archives"]
            )
        )
    else:
        raise DeserializationError("ListArchivesResponse.archives required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
