"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Job``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.id
    import aws_sdk_elastic_transcoder.types.job_input
    import aws_sdk_elastic_transcoder.types.job_inputs
    import aws_sdk_elastic_transcoder.types.job_output
    import aws_sdk_elastic_transcoder.types.job_outputs
    import aws_sdk_elastic_transcoder.types.job_status
    import aws_sdk_elastic_transcoder.types.key
    import aws_sdk_elastic_transcoder.types.playlists
    import aws_sdk_elastic_transcoder.types.string
    import aws_sdk_elastic_transcoder.types.timing
    import aws_sdk_elastic_transcoder.types.user_metadata


class Job(TypedDict):
    id: NotRequired["aws_sdk_elastic_transcoder.types.id.Id"]
    """<p>The identifier that Elastic Transcoder assigned to the job. You use this value to get settings for the job or to delete the job.</p>"""
    arn: NotRequired["aws_sdk_elastic_transcoder.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the job.</p>"""
    pipeline_id: NotRequired["aws_sdk_elastic_transcoder.types.id.Id"]
    """<p> The <code>Id</code> of the pipeline that you want Elastic Transcoder to use for transcoding. The pipeline determines several settings, including the Amazon S3 bucket from which Elastic Transcoder gets the files to transcode and the bucket into which Elastic Transcoder puts the transcoded files. </p>"""
    input: NotRequired["aws_sdk_elastic_transcoder.types.job_input.JobInput"]
    """<p>A section of the request or response body that provides information about the file that is being transcoded.</p>"""
    inputs: NotRequired["aws_sdk_elastic_transcoder.types.job_inputs.JobInputs"]
    """<p>Information about the files that you're transcoding. If you specified multiple files for this job, Elastic Transcoder stitches the files together to make one output.</p>"""
    output: NotRequired["aws_sdk_elastic_transcoder.types.job_output.JobOutput"]
    """<p>If you specified one output for a job, information about that output. If you specified multiple outputs for a job, the Output object lists information about the first output. This duplicates the information that is listed for the first output in the Outputs object.</p> <important> <p>Outputs recommended instead.</p> </important> <p>A section of the request or response body that provides information about the transcoded (target) file. </p>"""
    outputs: NotRequired["aws_sdk_elastic_transcoder.types.job_outputs.JobOutputs"]
    """<p>Information about the output files. We recommend that you use the <code>Outputs</code> syntax for all jobs, even when you want Elastic Transcoder to transcode a file into only one format. Do not use both the <code>Outputs</code> and <code>Output</code> syntaxes in the same request. You can create a maximum of 30 outputs per job. </p> <p>If you specify more than one output for a job, Elastic Transcoder creates the files for each output in the order in which you specify them in the job.</p>"""
    output_key_prefix: NotRequired["aws_sdk_elastic_transcoder.types.key.Key"]
    """<p>The value, if any, that you want Elastic Transcoder to prepend to the names of all files that this job creates, including output files, thumbnails, and playlists. We recommend that you add a / or some other delimiter to the end of the <code>OutputKeyPrefix</code>.</p>"""
    playlists: NotRequired["aws_sdk_elastic_transcoder.types.playlists.Playlists"]
    """<important> <p>Outputs in Fragmented MP4 or MPEG-TS format only.</p> </important> <p>If you specify a preset in <code>PresetId</code> for which the value of <code>Container</code> is fmp4 (Fragmented MP4) or ts (MPEG-TS), <code>Playlists</code> contains information about the master playlists that you want Elastic Transcoder to create.</p> <p>The maximum number of master playlists in a job is 30.</p>"""
    status: NotRequired["aws_sdk_elastic_transcoder.types.job_status.JobStatus"]
    """<p> The status of the job: <code>Submitted</code>, <code>Progressing</code>, <code>Complete</code>, <code>Canceled</code>, or <code>Error</code>. </p>"""
    user_metadata: NotRequired[
        "aws_sdk_elastic_transcoder.types.user_metadata.UserMetadata"
    ]
    """<p>User-defined metadata that you want to associate with an Elastic Transcoder job. You specify metadata in <code>key/value</code> pairs, and you can add up to 10 <code>key/value</code> pairs per job. Elastic Transcoder does not guarantee that <code>key/value</code> pairs are returned in the same order in which you specify them.</p> <p>Metadata <code>keys</code> and <code>values</code> must use characters from the following list:</p> <ul> <li> <p> <code>0-9</code> </p> </li> <li> <p> <code>A-Z</code> and <code>a-z</code> </p> </li> <li> <p> <code>Space</code> </p> </li> <li> <p>The following symbols: <code>_.:/=+-%@</code> </p> </li> </ul>"""
    timing: NotRequired["aws_sdk_elastic_transcoder.types.timing.Timing"]
    """<p>Details about the timing of a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Job) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "pipeline_id" in value:
        out["PipelineId"] = value["pipeline_id"]
    if "input" in value:
        import aws_sdk_elastic_transcoder.types.job_input

        out["Input"] = aws_sdk_elastic_transcoder.types.job_input.serialize_json(
            value["input"]
        )
    if "inputs" in value:
        import aws_sdk_elastic_transcoder.types.job_inputs

        out["Inputs"] = aws_sdk_elastic_transcoder.types.job_inputs.serialize_json(
            value["inputs"]
        )
    if "output" in value:
        import aws_sdk_elastic_transcoder.types.job_output

        out["Output"] = aws_sdk_elastic_transcoder.types.job_output.serialize_json(
            value["output"]
        )
    if "outputs" in value:
        import aws_sdk_elastic_transcoder.types.job_outputs

        out["Outputs"] = aws_sdk_elastic_transcoder.types.job_outputs.serialize_json(
            value["outputs"]
        )
    if "output_key_prefix" in value:
        out["OutputKeyPrefix"] = value["output_key_prefix"]
    if "playlists" in value:
        import aws_sdk_elastic_transcoder.types.playlists

        out["Playlists"] = aws_sdk_elastic_transcoder.types.playlists.serialize_json(
            value["playlists"]
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "user_metadata" in value:
        import aws_sdk_elastic_transcoder.types.user_metadata

        out["UserMetadata"] = (
            aws_sdk_elastic_transcoder.types.user_metadata.serialize_json(
                value["user_metadata"]
            )
        )
    if "timing" in value:
        import aws_sdk_elastic_transcoder.types.timing

        out["Timing"] = aws_sdk_elastic_transcoder.types.timing.serialize_json(
            value["timing"]
        )
    return out


def deserialize_json(data: dict) -> Job:
    out: Job = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "PipelineId" in data:
        out["pipeline_id"] = data["PipelineId"]
    if "Input" in data:
        import aws_sdk_elastic_transcoder.types.job_input

        out["input"] = aws_sdk_elastic_transcoder.types.job_input.deserialize_json(
            data["Input"]
        )
    if "Inputs" in data:
        import aws_sdk_elastic_transcoder.types.job_inputs

        out["inputs"] = aws_sdk_elastic_transcoder.types.job_inputs.deserialize_json(
            data["Inputs"]
        )
    if "Output" in data:
        import aws_sdk_elastic_transcoder.types.job_output

        out["output"] = aws_sdk_elastic_transcoder.types.job_output.deserialize_json(
            data["Output"]
        )
    if "Outputs" in data:
        import aws_sdk_elastic_transcoder.types.job_outputs

        out["outputs"] = aws_sdk_elastic_transcoder.types.job_outputs.deserialize_json(
            data["Outputs"]
        )
    if "OutputKeyPrefix" in data:
        out["output_key_prefix"] = data["OutputKeyPrefix"]
    if "Playlists" in data:
        import aws_sdk_elastic_transcoder.types.playlists

        out["playlists"] = aws_sdk_elastic_transcoder.types.playlists.deserialize_json(
            data["Playlists"]
        )
    if "Status" in data:
        out["status"] = data["Status"]
    if "UserMetadata" in data:
        import aws_sdk_elastic_transcoder.types.user_metadata

        out["user_metadata"] = (
            aws_sdk_elastic_transcoder.types.user_metadata.deserialize_json(
                data["UserMetadata"]
            )
        )
    if "Timing" in data:
        import aws_sdk_elastic_transcoder.types.timing

        out["timing"] = aws_sdk_elastic_transcoder.types.timing.deserialize_json(
            data["Timing"]
        )
    return out
