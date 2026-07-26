"""Generated from Smithy shape ``com.amazonaws.kafka#GetCompatibleKafkaVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__list_of_compatible_kafka_version


class GetCompatibleKafkaVersionsResponse(TypedDict, closed=True):
    compatible_kafka_versions: NotRequired[
        "capo_kafka.types.__list_of_compatible_kafka_version.__listOfCompatibleKafkaVersion"
    ]
    """<p>A list of CompatibleKafkaVersion objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCompatibleKafkaVersionsResponse) -> dict:
    out: dict = {}
    if "compatible_kafka_versions" in value:
        import capo_kafka.types.__list_of_compatible_kafka_version

        out["compatibleKafkaVersions"] = (
            capo_kafka.types.__list_of_compatible_kafka_version.serialize_json(
                value["compatible_kafka_versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCompatibleKafkaVersionsResponse:
    out: GetCompatibleKafkaVersionsResponse = {}  # type: ignore[typeddict-item]
    if "compatibleKafkaVersions" in data:
        import capo_kafka.types.__list_of_compatible_kafka_version

        out["compatible_kafka_versions"] = (
            capo_kafka.types.__list_of_compatible_kafka_version.deserialize_json(
                data["compatibleKafkaVersions"]
            )
        )
    return out
