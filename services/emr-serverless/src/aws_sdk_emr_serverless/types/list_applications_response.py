"""Generated from Smithy shape ``com.amazonaws.emrserverless#ListApplicationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_list
    import aws_sdk_emr_serverless.types.next_token


class ListApplicationsResponse(TypedDict):
    applications: "aws_sdk_emr_serverless.types.application_list.ApplicationList"
    """<p>The output lists the specified applications.</p>"""
    next_token: NotRequired["aws_sdk_emr_serverless.types.next_token.NextToken"]
    """<p>The output displays the token for the next set of application results. This is required for pagination and is available as a response of the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_emr_serverless.types.application_list

    out["applications"] = aws_sdk_emr_serverless.types.application_list.serialize_json(
        value["applications"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if "applications" in data:
        import aws_sdk_emr_serverless.types.application_list

        out["applications"] = (
            aws_sdk_emr_serverless.types.application_list.deserialize_json(
                data["applications"]
            )
        )
    else:
        raise DeserializationError("ListApplicationsResponse.applications required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
