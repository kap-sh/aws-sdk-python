"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Playlist``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.description
    import capo_elastic_transcoder.types.filename
    import capo_elastic_transcoder.types.hls_content_protection
    import capo_elastic_transcoder.types.job_status
    import capo_elastic_transcoder.types.output_keys
    import capo_elastic_transcoder.types.play_ready_drm
    import capo_elastic_transcoder.types.playlist_format


class Playlist(TypedDict, closed=True):
    name: NotRequired["capo_elastic_transcoder.types.filename.Filename"]
    """<p>The name that you want Elastic Transcoder to assign to the master playlist, for example, nyc-vacation.m3u8. If the name includes a <code>/</code> character, the section of the name before the last <code>/</code> must be identical for all <code>Name</code> objects. If you create more than one master playlist, the values of all <code>Name</code> objects must be unique.</p> <note> <p>Elastic Transcoder automatically appends the relevant file extension to the file name (<code>.m3u8</code> for <code>HLSv3</code> and <code>HLSv4</code> playlists, and <code>.ism</code> and <code>.ismc</code> for <code>Smooth</code> playlists). If you include a file extension in <code>Name</code>, the file name will have two extensions.</p> </note>"""
    format: NotRequired["capo_elastic_transcoder.types.playlist_format.PlaylistFormat"]
    """<p>The format of the output playlist. Valid formats include <code>HLSv3</code>, <code>HLSv4</code>, and <code>Smooth</code>.</p>"""
    output_keys: NotRequired["capo_elastic_transcoder.types.output_keys.OutputKeys"]
    """<p>For each output in this job that you want to include in a master playlist, the value of the Outputs:Key object.</p> <ul> <li> <p>If your output is not <code>HLS</code> or does not have a segment duration set, the name of the output file is a concatenation of <code>OutputKeyPrefix</code> and <code>Outputs:Key</code>:</p> <p>OutputKeyPrefix<code>Outputs:Key</code> </p> </li> <li> <p>If your output is <code>HLSv3</code> and has a segment duration set, or is not included in a playlist, Elastic Transcoder creates an output playlist file with a file extension of <code>.m3u8</code>, and a series of <code>.ts</code> files that include a five-digit sequential counter beginning with 00000:</p> <p>OutputKeyPrefix<code>Outputs:Key</code>.m3u8</p> <p>OutputKeyPrefix<code>Outputs:Key</code>00000.ts</p> </li> <li> <p>If your output is <code>HLSv4</code>, has a segment duration set, and is included in an <code>HLSv4</code> playlist, Elastic Transcoder creates an output playlist file with a file extension of <code>_v4.m3u8</code>. If the output is video, Elastic Transcoder also creates an output file with an extension of <code>_iframe.m3u8</code>:</p> <p>OutputKeyPrefix<code>Outputs:Key</code>_v4.m3u8</p> <p>OutputKeyPrefix<code>Outputs:Key</code>_iframe.m3u8</p> <p>OutputKeyPrefix<code>Outputs:Key</code>.ts</p> </li> </ul> <p>Elastic Transcoder automatically appends the relevant file extension to the file name. If you include a file extension in Output Key, the file name will have two extensions.</p> <p>If you include more than one output in a playlist, any segment duration settings, clip settings, or caption settings must be the same for all outputs in the playlist. For <code>Smooth</code> playlists, the <code>Audio:Profile</code>, <code>Video:Profile</code>, and <code>Video:FrameRate</code> to <code>Video:KeyframesMaxDist</code> ratio must be the same for all outputs.</p>"""
    hls_content_protection: NotRequired[
        "capo_elastic_transcoder.types.hls_content_protection.HlsContentProtection"
    ]
    """<p>The HLS content protection settings, if any, that you want Elastic Transcoder to apply to the output files associated with this playlist.</p>"""
    play_ready_drm: NotRequired[
        "capo_elastic_transcoder.types.play_ready_drm.PlayReadyDrm"
    ]
    """<p>The DRM settings, if any, that you want Elastic Transcoder to apply to the output files associated with this playlist.</p>"""
    status: NotRequired["capo_elastic_transcoder.types.job_status.JobStatus"]
    """<p>The status of the job with which the playlist is associated.</p>"""
    status_detail: NotRequired["capo_elastic_transcoder.types.description.Description"]
    """<p>Information that further explains the status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Playlist) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "format" in value:
        out["Format"] = value["format"]
    if "output_keys" in value:
        import capo_elastic_transcoder.types.output_keys

        out["OutputKeys"] = capo_elastic_transcoder.types.output_keys.serialize_json(
            value["output_keys"]
        )
    if "hls_content_protection" in value:
        import capo_elastic_transcoder.types.hls_content_protection

        out["HlsContentProtection"] = (
            capo_elastic_transcoder.types.hls_content_protection.serialize_json(
                value["hls_content_protection"]
            )
        )
    if "play_ready_drm" in value:
        import capo_elastic_transcoder.types.play_ready_drm

        out["PlayReadyDrm"] = (
            capo_elastic_transcoder.types.play_ready_drm.serialize_json(
                value["play_ready_drm"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "status_detail" in value:
        out["StatusDetail"] = value["status_detail"]
    return out


def deserialize_json(data: dict) -> Playlist:
    out: Playlist = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Format" in data:
        out["format"] = data["Format"]
    if "OutputKeys" in data:
        import capo_elastic_transcoder.types.output_keys

        out["output_keys"] = capo_elastic_transcoder.types.output_keys.deserialize_json(
            data["OutputKeys"]
        )
    if "HlsContentProtection" in data:
        import capo_elastic_transcoder.types.hls_content_protection

        out["hls_content_protection"] = (
            capo_elastic_transcoder.types.hls_content_protection.deserialize_json(
                data["HlsContentProtection"]
            )
        )
    if "PlayReadyDrm" in data:
        import capo_elastic_transcoder.types.play_ready_drm

        out["play_ready_drm"] = (
            capo_elastic_transcoder.types.play_ready_drm.deserialize_json(
                data["PlayReadyDrm"]
            )
        )
    if "Status" in data:
        out["status"] = data["Status"]
    if "StatusDetail" in data:
        out["status_detail"] = data["StatusDetail"]
    return out
