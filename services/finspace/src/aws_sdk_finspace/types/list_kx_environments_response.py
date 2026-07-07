"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxEnvironmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_environment_list
    import aws_sdk_finspace.types.pagination_token


class ListKxEnvironmentsResponse(TypedDict, closed=True):
    environments: NotRequired[
        "aws_sdk_finspace.types.kx_environment_list.KxEnvironmentList"
    ]
    """<p>A list of environments in an account.</p>"""
    next_token: NotRequired["aws_sdk_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxEnvironmentsResponse) -> dict:
    out: dict = {}
    if "environments" in value:
        import aws_sdk_finspace.types.kx_environment_list

        out["environments"] = aws_sdk_finspace.types.kx_environment_list.serialize_json(
            value["environments"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKxEnvironmentsResponse:
    out: ListKxEnvironmentsResponse = {}  # type: ignore[typeddict-item]
    if "environments" in data:
        import aws_sdk_finspace.types.kx_environment_list

        out["environments"] = (
            aws_sdk_finspace.types.kx_environment_list.deserialize_json(
                data["environments"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
