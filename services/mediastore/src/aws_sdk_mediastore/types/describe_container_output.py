"""Generated from Smithy shape ``com.amazonaws.mediastore#DescribeContainerOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.container


class DescribeContainerOutput(TypedDict):
    container: NotRequired["aws_sdk_mediastore.types.container.Container"]
    """<p>The name of the queried container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeContainerOutput) -> dict:
    out: dict = {}
    if "container" in value:
        import aws_sdk_mediastore.types.container

        out["Container"] = aws_sdk_mediastore.types.container.serialize_aws_json_1_1(
            value["container"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeContainerOutput:
    out: DescribeContainerOutput = {}  # type: ignore[typeddict-item]
    if "Container" in data:
        import aws_sdk_mediastore.types.container

        out["container"] = aws_sdk_mediastore.types.container.deserialize_aws_json_1_1(
            data["Container"]
        )
    return out
