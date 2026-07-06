"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CanDbcDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.interface_id
    import aws_sdk_iotfleetwise.types.model_signals_map
    import aws_sdk_iotfleetwise.types.network_files_list


class CanDbcDefinition(TypedDict, closed=True):
    network_interface: "aws_sdk_iotfleetwise.types.interface_id.InterfaceId"
    """<p>Contains information about a network interface.</p>"""
    can_dbc_files: "aws_sdk_iotfleetwise.types.network_files_list.NetworkFilesList"
    """<p>A list of DBC files. You can upload only one DBC file for each network interface and specify up to five (inclusive) files in the list. The DBC file can be a maximum size of 200 MB.</p>"""
    signals_map: NotRequired[
        "aws_sdk_iotfleetwise.types.model_signals_map.ModelSignalsMap"
    ]
    """<p>Pairs every signal specified in your vehicle model with a signal decoder.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CanDbcDefinition) -> dict:
    out: dict = {}
    out["networkInterface"] = value["network_interface"]
    import aws_sdk_iotfleetwise.types.network_files_list

    out["canDbcFiles"] = (
        aws_sdk_iotfleetwise.types.network_files_list.serialize_aws_json_1_0(
            value["can_dbc_files"]
        )
    )
    if "signals_map" in value:
        import aws_sdk_iotfleetwise.types.model_signals_map

        out["signalsMap"] = (
            aws_sdk_iotfleetwise.types.model_signals_map.serialize_aws_json_1_0(
                value["signals_map"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CanDbcDefinition:
    out: CanDbcDefinition = {}  # type: ignore[typeddict-item]
    if "networkInterface" in data:
        out["network_interface"] = data["networkInterface"]
    else:
        raise DeserializationError("CanDbcDefinition.network_interface required")
    if "canDbcFiles" in data:
        import aws_sdk_iotfleetwise.types.network_files_list

        out["can_dbc_files"] = (
            aws_sdk_iotfleetwise.types.network_files_list.deserialize_aws_json_1_0(
                data["canDbcFiles"]
            )
        )
    else:
        raise DeserializationError("CanDbcDefinition.can_dbc_files required")
    if "signalsMap" in data:
        import aws_sdk_iotfleetwise.types.model_signals_map

        out["signals_map"] = (
            aws_sdk_iotfleetwise.types.model_signals_map.deserialize_aws_json_1_0(
                data["signalsMap"]
            )
        )
    return out
