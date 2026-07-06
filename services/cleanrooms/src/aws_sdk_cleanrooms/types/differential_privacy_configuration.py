"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.differential_privacy_column_list


class DifferentialPrivacyConfiguration(TypedDict, closed=True):
    columns: "aws_sdk_cleanrooms.types.differential_privacy_column_list.DifferentialPrivacyColumnList"
    """<p>The name of the column (such as user_id) that contains the unique identifier of your users whose privacy you want to protect. If you want to turn on diﬀerential privacy for two or more tables in a collaboration, you must conﬁgure the same column as the user identiﬁer column in both analysis rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DifferentialPrivacyConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.differential_privacy_column_list

    out["columns"] = (
        aws_sdk_cleanrooms.types.differential_privacy_column_list.serialize_json(
            value["columns"]
        )
    )
    return out


def deserialize_json(data: dict) -> DifferentialPrivacyConfiguration:
    out: DifferentialPrivacyConfiguration = {}  # type: ignore[typeddict-item]
    if "columns" in data:
        import aws_sdk_cleanrooms.types.differential_privacy_column_list

        out["columns"] = (
            aws_sdk_cleanrooms.types.differential_privacy_column_list.deserialize_json(
                data["columns"]
            )
        )
    else:
        raise DeserializationError("DifferentialPrivacyConfiguration.columns required")
    return out
