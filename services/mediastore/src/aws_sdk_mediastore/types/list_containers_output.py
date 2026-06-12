"""Generated from Smithy shape ``com.amazonaws.mediastore#ListContainersOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.container_list
    import aws_sdk_mediastore.types.pagination_token


class ListContainersOutput(TypedDict):
    containers: "aws_sdk_mediastore.types.container_list.ContainerList"
    """<p>The names of the containers.</p>"""
    next_token: NotRequired["aws_sdk_mediastore.types.pagination_token.PaginationToken"]
    """<p> <code>NextToken</code> is the token to use in the next call to <code>ListContainers</code>. This token is returned only if you included the <code>MaxResults</code> tag in the original command, and only if there are still containers to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContainersOutput) -> dict:
    out: dict = {}
    import aws_sdk_mediastore.types.container_list

    out["Containers"] = aws_sdk_mediastore.types.container_list.serialize_aws_json_1_1(
        value["containers"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContainersOutput:
    out: ListContainersOutput = {}  # type: ignore[typeddict-item]
    if "Containers" in data:
        import aws_sdk_mediastore.types.container_list

        out["containers"] = (
            aws_sdk_mediastore.types.container_list.deserialize_aws_json_1_1(
                data["Containers"]
            )
        )
    else:
        raise DeserializationError("ListContainersOutput.containers required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
