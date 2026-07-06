"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#IteratorDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.iterator_position


class IteratorDescription(TypedDict, closed=True):
    iterator_position: NotRequired[
        "aws_sdk_keyspacesstreams.types.iterator_position.IteratorPosition"
    ]
    """<p> Indicates the current iterator's position within the shard. The possible values are: </p> <ul> <li> <p> <code>AT_TIP</code> - No more records are currently available.</p> </li> <li> <p> <code>BEHIND_TIP</code> - Additional records may be available.</p> </li> </ul> <p>Stream progresses in absence of customer records. <code>BEHIND_TIP</code> with an empty <code>changeRecords</code> list indicates the stream is progressing but no customer records are available at this position. Continue polling normally.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IteratorDescription) -> dict:
    out: dict = {}
    if "iterator_position" in value:
        import aws_sdk_keyspacesstreams.types.iterator_position

        out["iteratorPosition"] = (
            aws_sdk_keyspacesstreams.types.iterator_position.serialize_aws_json_1_0(
                value["iterator_position"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IteratorDescription:
    out: IteratorDescription = {}  # type: ignore[typeddict-item]
    if "iteratorPosition" in data:
        import aws_sdk_keyspacesstreams.types.iterator_position

        out["iterator_position"] = (
            aws_sdk_keyspacesstreams.types.iterator_position.deserialize_aws_json_1_0(
                data["iteratorPosition"]
            )
        )
    return out
