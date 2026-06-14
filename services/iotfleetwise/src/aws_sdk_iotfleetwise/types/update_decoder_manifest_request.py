"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateDecoderManifestRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.default_for_unmapped_signals_type
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.fqns
    import aws_sdk_iotfleetwise.types.interface_ids
    import aws_sdk_iotfleetwise.types.manifest_status
    import aws_sdk_iotfleetwise.types.network_interfaces
    import aws_sdk_iotfleetwise.types.resource_name
    import aws_sdk_iotfleetwise.types.signal_decoders


class UpdateDecoderManifestRequest(TypedDict):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the decoder manifest to update.</p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p> A brief description of the decoder manifest to update. </p>"""
    signal_decoders_to_add: NotRequired[
        "aws_sdk_iotfleetwise.types.signal_decoders.SignalDecoders"
    ]
    """<p> A list of information about decoding additional signals to add to the decoder manifest. </p>"""
    signal_decoders_to_update: NotRequired[
        "aws_sdk_iotfleetwise.types.signal_decoders.SignalDecoders"
    ]
    """<p> A list of updated information about decoding signals to update in the decoder manifest. </p>"""
    signal_decoders_to_remove: NotRequired["aws_sdk_iotfleetwise.types.fqns.Fqns"]
    """<p> A list of signal decoders to remove from the decoder manifest. </p>"""
    network_interfaces_to_add: NotRequired[
        "aws_sdk_iotfleetwise.types.network_interfaces.NetworkInterfaces"
    ]
    """<p> A list of information about the network interfaces to add to the decoder manifest. </p>"""
    network_interfaces_to_update: NotRequired[
        "aws_sdk_iotfleetwise.types.network_interfaces.NetworkInterfaces"
    ]
    """<p> A list of information about the network interfaces to update in the decoder manifest. </p>"""
    network_interfaces_to_remove: NotRequired[
        "aws_sdk_iotfleetwise.types.interface_ids.InterfaceIds"
    ]
    """<p> A list of network interfaces to remove from the decoder manifest.</p>"""
    status: NotRequired["aws_sdk_iotfleetwise.types.manifest_status.ManifestStatus"]
    """<p> The state of the decoder manifest. If the status is <code>ACTIVE</code>, the decoder manifest can't be edited. If the status is <code>DRAFT</code>, you can edit the decoder manifest. </p>"""
    default_for_unmapped_signals: NotRequired[
        "aws_sdk_iotfleetwise.types.default_for_unmapped_signals_type.DefaultForUnmappedSignalsType"
    ]
    r"""<p>Use default decoders for all unmapped signals in the model. You don't need to provide any detailed decoding information.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html\">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDecoderManifestRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "signal_decoders_to_add" in value:
        import aws_sdk_iotfleetwise.types.signal_decoders

        out["signalDecodersToAdd"] = (
            aws_sdk_iotfleetwise.types.signal_decoders.serialize_aws_json_1_0(
                value["signal_decoders_to_add"]
            )
        )
    if "signal_decoders_to_update" in value:
        import aws_sdk_iotfleetwise.types.signal_decoders

        out["signalDecodersToUpdate"] = (
            aws_sdk_iotfleetwise.types.signal_decoders.serialize_aws_json_1_0(
                value["signal_decoders_to_update"]
            )
        )
    if "signal_decoders_to_remove" in value:
        import aws_sdk_iotfleetwise.types.fqns

        out["signalDecodersToRemove"] = (
            aws_sdk_iotfleetwise.types.fqns.serialize_aws_json_1_0(
                value["signal_decoders_to_remove"]
            )
        )
    if "network_interfaces_to_add" in value:
        import aws_sdk_iotfleetwise.types.network_interfaces

        out["networkInterfacesToAdd"] = (
            aws_sdk_iotfleetwise.types.network_interfaces.serialize_aws_json_1_0(
                value["network_interfaces_to_add"]
            )
        )
    if "network_interfaces_to_update" in value:
        import aws_sdk_iotfleetwise.types.network_interfaces

        out["networkInterfacesToUpdate"] = (
            aws_sdk_iotfleetwise.types.network_interfaces.serialize_aws_json_1_0(
                value["network_interfaces_to_update"]
            )
        )
    if "network_interfaces_to_remove" in value:
        import aws_sdk_iotfleetwise.types.interface_ids

        out["networkInterfacesToRemove"] = (
            aws_sdk_iotfleetwise.types.interface_ids.serialize_aws_json_1_0(
                value["network_interfaces_to_remove"]
            )
        )
    if "status" in value:
        import aws_sdk_iotfleetwise.types.manifest_status

        out["status"] = (
            aws_sdk_iotfleetwise.types.manifest_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "default_for_unmapped_signals" in value:
        import aws_sdk_iotfleetwise.types.default_for_unmapped_signals_type

        out["defaultForUnmappedSignals"] = (
            aws_sdk_iotfleetwise.types.default_for_unmapped_signals_type.serialize_aws_json_1_0(
                value["default_for_unmapped_signals"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateDecoderManifestRequest:
    out: UpdateDecoderManifestRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "signalDecodersToAdd" in data:
        import aws_sdk_iotfleetwise.types.signal_decoders

        out["signal_decoders_to_add"] = (
            aws_sdk_iotfleetwise.types.signal_decoders.deserialize_aws_json_1_0(
                data["signalDecodersToAdd"]
            )
        )
    if "signalDecodersToUpdate" in data:
        import aws_sdk_iotfleetwise.types.signal_decoders

        out["signal_decoders_to_update"] = (
            aws_sdk_iotfleetwise.types.signal_decoders.deserialize_aws_json_1_0(
                data["signalDecodersToUpdate"]
            )
        )
    if "signalDecodersToRemove" in data:
        import aws_sdk_iotfleetwise.types.fqns

        out["signal_decoders_to_remove"] = (
            aws_sdk_iotfleetwise.types.fqns.deserialize_aws_json_1_0(
                data["signalDecodersToRemove"]
            )
        )
    if "networkInterfacesToAdd" in data:
        import aws_sdk_iotfleetwise.types.network_interfaces

        out["network_interfaces_to_add"] = (
            aws_sdk_iotfleetwise.types.network_interfaces.deserialize_aws_json_1_0(
                data["networkInterfacesToAdd"]
            )
        )
    if "networkInterfacesToUpdate" in data:
        import aws_sdk_iotfleetwise.types.network_interfaces

        out["network_interfaces_to_update"] = (
            aws_sdk_iotfleetwise.types.network_interfaces.deserialize_aws_json_1_0(
                data["networkInterfacesToUpdate"]
            )
        )
    if "networkInterfacesToRemove" in data:
        import aws_sdk_iotfleetwise.types.interface_ids

        out["network_interfaces_to_remove"] = (
            aws_sdk_iotfleetwise.types.interface_ids.deserialize_aws_json_1_0(
                data["networkInterfacesToRemove"]
            )
        )
    if "status" in data:
        import aws_sdk_iotfleetwise.types.manifest_status

        out["status"] = (
            aws_sdk_iotfleetwise.types.manifest_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "defaultForUnmappedSignals" in data:
        import aws_sdk_iotfleetwise.types.default_for_unmapped_signals_type

        out["default_for_unmapped_signals"] = (
            aws_sdk_iotfleetwise.types.default_for_unmapped_signals_type.deserialize_aws_json_1_0(
                data["defaultForUnmappedSignals"]
            )
        )
    return out
