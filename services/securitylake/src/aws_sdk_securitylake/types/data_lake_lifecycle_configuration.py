"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeLifecycleConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.data_lake_lifecycle_expiration
    import aws_sdk_securitylake.types.data_lake_lifecycle_transition_list


class DataLakeLifecycleConfiguration(TypedDict):
    expiration: NotRequired[
        "aws_sdk_securitylake.types.data_lake_lifecycle_expiration.DataLakeLifecycleExpiration"
    ]
    """<p>Provides data expiration details of Amazon Security Lake object.</p>"""
    transitions: NotRequired[
        "aws_sdk_securitylake.types.data_lake_lifecycle_transition_list.DataLakeLifecycleTransitionList"
    ]
    """<p>Provides data storage transition details of Amazon Security Lake object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeLifecycleConfiguration) -> dict:
    out: dict = {}
    if "expiration" in value:
        import aws_sdk_securitylake.types.data_lake_lifecycle_expiration

        out["expiration"] = (
            aws_sdk_securitylake.types.data_lake_lifecycle_expiration.serialize_json(
                value["expiration"]
            )
        )
    if "transitions" in value:
        import aws_sdk_securitylake.types.data_lake_lifecycle_transition_list

        out["transitions"] = (
            aws_sdk_securitylake.types.data_lake_lifecycle_transition_list.serialize_json(
                value["transitions"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataLakeLifecycleConfiguration:
    out: DataLakeLifecycleConfiguration = {}  # type: ignore[typeddict-item]
    if "expiration" in data:
        import aws_sdk_securitylake.types.data_lake_lifecycle_expiration

        out["expiration"] = (
            aws_sdk_securitylake.types.data_lake_lifecycle_expiration.deserialize_json(
                data["expiration"]
            )
        )
    if "transitions" in data:
        import aws_sdk_securitylake.types.data_lake_lifecycle_transition_list

        out["transitions"] = (
            aws_sdk_securitylake.types.data_lake_lifecycle_transition_list.deserialize_json(
                data["transitions"]
            )
        )
    return out
