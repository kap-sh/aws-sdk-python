"""Generated from Smithy shape ``com.amazonaws.wafv2#VersionsToPublish``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.version_key_string
    import capo_wafv2.types.version_to_publish

VersionsToPublish: TypeAlias = dict[
    "capo_wafv2.types.version_key_string.VersionKeyString",
    "capo_wafv2.types.version_to_publish.VersionToPublish",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: VersionsToPublish) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_wafv2.types.version_to_publish

        out[key] = capo_wafv2.types.version_to_publish.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> VersionsToPublish:
    out: VersionsToPublish = {}
    for key, value in data.items():
        import capo_wafv2.types.version_to_publish

        out[key] = capo_wafv2.types.version_to_publish.deserialize_aws_json_1_1(value)
    return out
