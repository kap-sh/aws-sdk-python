"""Generated from Smithy shape ``com.amazonaws.mediastore#CreateContainerOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediastore.types.container


class CreateContainerOutput(TypedDict, closed=True):
    container: "capo_mediastore.types.container.Container"
    """<p>ContainerARN: The Amazon Resource Name (ARN) of the newly created container. The ARN has the following format: arn:aws:<region>:<account that owns this container>:container/<name of container>. For example: arn:aws:mediastore:us-west-2:111122223333:container/movies </p> <p>ContainerName: The container name as specified in the request.</p> <p>CreationTime: Unix time stamp.</p> <p>Status: The status of container creation or deletion. The status is one of the following: <code>CREATING</code>, <code>ACTIVE</code>, or <code>DELETING</code>. While the service is creating the container, the status is <code>CREATING</code>. When an endpoint is available, the status changes to <code>ACTIVE</code>.</p> <p>The return value does not include the container's endpoint. To make downstream requests, you must obtain this value by using <a>DescribeContainer</a> or <a>ListContainers</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContainerOutput) -> dict:
    out: dict = {}
    import capo_mediastore.types.container

    out["Container"] = capo_mediastore.types.container.serialize_aws_json_1_1(
        value["container"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContainerOutput:
    out: CreateContainerOutput = {}  # type: ignore[typeddict-item]
    if "Container" in data:
        import capo_mediastore.types.container

        out["container"] = capo_mediastore.types.container.deserialize_aws_json_1_1(
            data["Container"]
        )
    else:
        raise DeserializationError("CreateContainerOutput.container required")
    return out
