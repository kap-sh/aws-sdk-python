"""Generated from Smithy shape ``com.amazonaws.connect#GranularAccessControlConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_access_control_configuration


class GranularAccessControlConfiguration(TypedDict, closed=True):
    data_table_access_control_configuration: NotRequired[
        "aws_sdk_connect.types.data_table_access_control_configuration.DataTableAccessControlConfiguration"
    ]
    """<p>The access control configuration for data tables.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GranularAccessControlConfiguration) -> dict:
    out: dict = {}
    if "data_table_access_control_configuration" in value:
        import aws_sdk_connect.types.data_table_access_control_configuration

        out["DataTableAccessControlConfiguration"] = (
            aws_sdk_connect.types.data_table_access_control_configuration.serialize_json(
                value["data_table_access_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GranularAccessControlConfiguration:
    out: GranularAccessControlConfiguration = {}  # type: ignore[typeddict-item]
    if "DataTableAccessControlConfiguration" in data:
        import aws_sdk_connect.types.data_table_access_control_configuration

        out["data_table_access_control_configuration"] = (
            aws_sdk_connect.types.data_table_access_control_configuration.deserialize_json(
                data["DataTableAccessControlConfiguration"]
            )
        )
    return out
