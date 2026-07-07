"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexProgramPacketIdentifiersMap``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer
    import aws_sdk_medialive.types.__list_of__integer


class MultiplexProgramPacketIdentifiersMap(TypedDict, closed=True):
    audio_pids: NotRequired[
        "aws_sdk_medialive.types.__list_of__integer.__listOf__integer"
    ]
    dvb_sub_pids: NotRequired[
        "aws_sdk_medialive.types.__list_of__integer.__listOf__integer"
    ]
    dvb_teletext_pid: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    etv_platform_pid: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    etv_signal_pid: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    klv_data_pids: NotRequired[
        "aws_sdk_medialive.types.__list_of__integer.__listOf__integer"
    ]
    pcr_pid: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    pmt_pid: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    private_metadata_pid: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    scte27_pids: NotRequired[
        "aws_sdk_medialive.types.__list_of__integer.__listOf__integer"
    ]
    scte35_pid: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    timed_metadata_pid: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    video_pid: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    arib_captions_pid: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    dvb_teletext_pids: NotRequired[
        "aws_sdk_medialive.types.__list_of__integer.__listOf__integer"
    ]
    ecm_pid: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    smpte2038_pid: NotRequired["aws_sdk_medialive.types.__integer.__integer"]


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexProgramPacketIdentifiersMap) -> dict:
    out: dict = {}
    if "audio_pids" in value:
        import aws_sdk_medialive.types.__list_of__integer

        out["audioPids"] = aws_sdk_medialive.types.__list_of__integer.serialize_json(
            value["audio_pids"]
        )
    if "dvb_sub_pids" in value:
        import aws_sdk_medialive.types.__list_of__integer

        out["dvbSubPids"] = aws_sdk_medialive.types.__list_of__integer.serialize_json(
            value["dvb_sub_pids"]
        )
    if "dvb_teletext_pid" in value:
        out["dvbTeletextPid"] = value["dvb_teletext_pid"]
    if "etv_platform_pid" in value:
        out["etvPlatformPid"] = value["etv_platform_pid"]
    if "etv_signal_pid" in value:
        out["etvSignalPid"] = value["etv_signal_pid"]
    if "klv_data_pids" in value:
        import aws_sdk_medialive.types.__list_of__integer

        out["klvDataPids"] = aws_sdk_medialive.types.__list_of__integer.serialize_json(
            value["klv_data_pids"]
        )
    if "pcr_pid" in value:
        out["pcrPid"] = value["pcr_pid"]
    if "pmt_pid" in value:
        out["pmtPid"] = value["pmt_pid"]
    if "private_metadata_pid" in value:
        out["privateMetadataPid"] = value["private_metadata_pid"]
    if "scte27_pids" in value:
        import aws_sdk_medialive.types.__list_of__integer

        out["scte27Pids"] = aws_sdk_medialive.types.__list_of__integer.serialize_json(
            value["scte27_pids"]
        )
    if "scte35_pid" in value:
        out["scte35Pid"] = value["scte35_pid"]
    if "timed_metadata_pid" in value:
        out["timedMetadataPid"] = value["timed_metadata_pid"]
    if "video_pid" in value:
        out["videoPid"] = value["video_pid"]
    if "arib_captions_pid" in value:
        out["aribCaptionsPid"] = value["arib_captions_pid"]
    if "dvb_teletext_pids" in value:
        import aws_sdk_medialive.types.__list_of__integer

        out["dvbTeletextPids"] = (
            aws_sdk_medialive.types.__list_of__integer.serialize_json(
                value["dvb_teletext_pids"]
            )
        )
    if "ecm_pid" in value:
        out["ecmPid"] = value["ecm_pid"]
    if "smpte2038_pid" in value:
        out["smpte2038Pid"] = value["smpte2038_pid"]
    return out


def deserialize_json(data: dict) -> MultiplexProgramPacketIdentifiersMap:
    out: MultiplexProgramPacketIdentifiersMap = {}  # type: ignore[typeddict-item]
    if "audioPids" in data:
        import aws_sdk_medialive.types.__list_of__integer

        out["audio_pids"] = aws_sdk_medialive.types.__list_of__integer.deserialize_json(
            data["audioPids"]
        )
    if "dvbSubPids" in data:
        import aws_sdk_medialive.types.__list_of__integer

        out["dvb_sub_pids"] = (
            aws_sdk_medialive.types.__list_of__integer.deserialize_json(
                data["dvbSubPids"]
            )
        )
    if "dvbTeletextPid" in data:
        out["dvb_teletext_pid"] = data["dvbTeletextPid"]
    if "etvPlatformPid" in data:
        out["etv_platform_pid"] = data["etvPlatformPid"]
    if "etvSignalPid" in data:
        out["etv_signal_pid"] = data["etvSignalPid"]
    if "klvDataPids" in data:
        import aws_sdk_medialive.types.__list_of__integer

        out["klv_data_pids"] = (
            aws_sdk_medialive.types.__list_of__integer.deserialize_json(
                data["klvDataPids"]
            )
        )
    if "pcrPid" in data:
        out["pcr_pid"] = data["pcrPid"]
    if "pmtPid" in data:
        out["pmt_pid"] = data["pmtPid"]
    if "privateMetadataPid" in data:
        out["private_metadata_pid"] = data["privateMetadataPid"]
    if "scte27Pids" in data:
        import aws_sdk_medialive.types.__list_of__integer

        out["scte27_pids"] = (
            aws_sdk_medialive.types.__list_of__integer.deserialize_json(
                data["scte27Pids"]
            )
        )
    if "scte35Pid" in data:
        out["scte35_pid"] = data["scte35Pid"]
    if "timedMetadataPid" in data:
        out["timed_metadata_pid"] = data["timedMetadataPid"]
    if "videoPid" in data:
        out["video_pid"] = data["videoPid"]
    if "aribCaptionsPid" in data:
        out["arib_captions_pid"] = data["aribCaptionsPid"]
    if "dvbTeletextPids" in data:
        import aws_sdk_medialive.types.__list_of__integer

        out["dvb_teletext_pids"] = (
            aws_sdk_medialive.types.__list_of__integer.deserialize_json(
                data["dvbTeletextPids"]
            )
        )
    if "ecmPid" in data:
        out["ecm_pid"] = data["ecmPid"]
    if "smpte2038Pid" in data:
        out["smpte2038_pid"] = data["smpte2038Pid"]
    return out
